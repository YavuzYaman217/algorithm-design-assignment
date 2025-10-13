"""
Test Wrapper - General Test Framework
======================================
Used to test any function with a test_cases.txt file.

Usage:
    wrapper = TestWrapper(function=my_function, test_file="test_cases.txt")
    wrapper.run_all_tests()
"""

import configparser
import ast
import time
from dataclasses import dataclass
from typing import Any, Callable
from pathlib import Path


@dataclass
class TestCase:
    """Represents a single test case."""
    description: str
    input: Any
    expected: Any
    test_number: int = 0


@dataclass
class TestResult:
    """Represents the result of a single test execution."""
    test_case: TestCase
    actual: Any
    passed: bool
    execution_time: float  # in milliseconds
    error: str = ""


class TestWrapper:
    """
    Test Wrapper - Tests functions with a test_cases.txt file.
    """
    
    def __init__(self, function: Callable, test_file: str):
        """
        Initialize the test wrapper.
        
        Args:
            function: The function to be tested
            test_file: Path to test_cases.txt file (relative or absolute)
        """
        self.function = function
        self.test_file = test_file
        self.test_cases = []
        self.results = []
        
    def load_tests(self) -> None:
        """Load test cases from the test file."""
        if not Path(self.test_file).exists():
            raise FileNotFoundError(f"Test file not found: {self.test_file}")
        
        parser = configparser.ConfigParser()
        parser.read(self.test_file, encoding='utf-8')
        
        test_number = 1
        
        for section in parser.sections():
            if section.startswith('TEST'):
                description = parser.get(section, 'description', fallback='No description')
                input_str = parser.get(section, 'input')
                expected_str = parser.get(section, 'expected')
                
                # Parse input and expected values safely
                try:
                    input_value = ast.literal_eval(input_str)
                except (ValueError, SyntaxError):
                    input_value = input_str
                
                try:
                    expected_value = ast.literal_eval(expected_str)
                except (ValueError, SyntaxError):
                    expected_value = expected_str
                
                test_case = TestCase(
                    description=description,
                    input=input_value,
                    expected=expected_value,
                    test_number=test_number
                )
                self.test_cases.append(test_case)
                test_number += 1
    
    def run_single_test(self, test_case: TestCase) -> TestResult:
        """
        Run a single test case.
        
        Args:
            test_case: The test case to run
            
        Returns:
            TestResult object
        """
        try:
            # Measure time
            start_time = time.perf_counter()
            actual = self.function(test_case.input)
            end_time = time.perf_counter()
            
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            # Check result
            passed = actual == test_case.expected
            
            return TestResult(
                test_case=test_case,
                actual=actual,
                passed=passed,
                execution_time=execution_time
            )
            
        except Exception as e:
            # In case of error
            return TestResult(
                test_case=test_case,
                actual=None,
                passed=False,
                execution_time=0.0,
                error=str(e)
            )
    
    def run_all_tests(self) -> None:
        """Run all tests and show results."""
        # Load test file
        print(f"Loading tests from: {self.test_file}")
        self.load_tests()
        print(f"✓ Loaded {len(self.test_cases)} test cases\n")
        
        # Run tests
        print("Running tests...")
        for test_case in self.test_cases:
            result = self.run_single_test(test_case)
            self.results.append(result)
        
        # Show results
        self.print_results()
    
    def print_results(self) -> None:
        """Print test results in a formatted way."""
        function_name = self.function.__name__
        
        # Header
        print("\n" + "=" * 80)
        print(f"TEST RESULTS: {function_name}()")
        print("=" * 80)
        print(f"Test File: {self.test_file}")
        print(f"Total Tests: {len(self.results)}")
        print("=" * 80 + "\n")
        
        # Test results table
        print(f"{'No':<4} {'Status':<8} {'Time':<10} {'Description':<30}")
        print("-" * 80)
        
        for result in self.results:
            status = "✓ PASS" if result.passed else "✗ FAIL"
            time_str = f"{result.execution_time:.4f}ms"
            desc = result.test_case.description[:30]
            
            print(f"{result.test_case.test_number:<4} {status:<8} {time_str:<10} {desc}")
            
            # Show details if test failed
            if not result.passed:
                print(f"     Input:    {result.test_case.input}")
                print(f"     Expected: {result.test_case.expected}")
                print(f"     Actual:   {result.actual}")
                if result.error:
                    print(f"     Error:    {result.error}")
                print()
        
        print("-" * 80)
        
        # Summary
        passed_count = sum(1 for r in self.results if r.passed)
        failed_count = len(self.results) - passed_count
        success_rate = (passed_count / len(self.results) * 100) if self.results else 0
        
        total_time = sum(r.execution_time for r in self.results)
        avg_time = total_time / len(self.results) if self.results else 0
        min_time = min(r.execution_time for r in self.results) if self.results else 0
        max_time = max(r.execution_time for r in self.results) if self.results else 0
        
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Total Tests:     {len(self.results)}")
        print(f"Passed:          {passed_count} ✓")
        print(f"Failed:          {failed_count} ✗")
        print(f"Success Rate:    {success_rate:.1f}%")
        print("-" * 80)
        print(f"Total Time:      {total_time:.4f}ms")
        print(f"Average Time:    {avg_time:.4f}ms")
        print(f"Min Time:        {min_time:.4f}ms")
        print(f"Max Time:        {max_time:.4f}ms")
        print("=" * 80 + "\n")



