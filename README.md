# Algorithm Design & Analysis - Course Projects

🇧 English | [🇹🇷 Türkçe](README_tr.md)

This repository contains algorithm design projects and implementations developed throughout the semester. Each project includes detailed algorithm descriptions, working code implementations, and comprehensive test cases.

## 📚 Course Information

**Course:** Algorithm Design and Analysis  
**Semester:** Fall 2025/2026  
**Focus Areas:** Problem solving, algorithm design, complexity analysis, optimization

## 🗂️ Repository Structure

```
Algorithm and Analysis/
│
├── README.md                    # Project documentation (English)
├── README_tr.md                 # Proje dokümantasyonu (Türkçe)
├── test_wrapper.py              # Universal test framework
│
└── week-01/                     # Weekly assignments
    ├── nearest-square/
    │   ├── algorithm.txt        # Algorithm description
    │   ├── nearest_square.py    # Implementation
    │   └── test_cases.txt       # Test cases
    │
    └── prime-finder/
        ├── algorithm.txt
        ├── prime_finder.py
        └── test_cases.txt
```

## 🧪 Test Framework

This repository includes a powerful **Test Wrapper** framework that automatically tests any function against test cases defined in `test_cases.txt` files.

### Features:
- ✅ Automatic test case loading from `.txt` files
- ⚡ Performance measurement (execution time)
- 📊 Detailed test reports with pass/fail status
- 🎯 Easy integration with any Python function

### Usage:

```python
from test_wrapper import TestWrapper

# Example: Test the nearest_square function
from week_01.nearest_square.nearest_square import nearest_square

wrapper = TestWrapper(
    function=nearest_square,
    test_file="week-01/nearest-square/test_cases.txt"
)
wrapper.run_all_tests()
```

### Test Case Format:

Test cases are defined in `test_cases.txt` files using INI format:

```ini
[TEST1]
description = Basic positive number
input = 10
expected = 9

[TEST2]
description = Perfect square
input = 16
expected = 16
```

## 📝 Week 01 - Assignments

### 1. Nearest Perfect Square
**Problem:** Find the nearest perfect square to a given positive integer N.

**Algorithm Highlights:**
- Calculate √N
- Find lower and upper perfect squares
- Determine the nearest by comparing distances

**File:** `week-01/nearest-square/nearest_square.py`

### 2. Prime Number Finder
**Problem:** Find all prime numbers up to a given positive integer N.

**Algorithm Highlights:**
- Trial division method
- Optimization using √i limit
- Efficient prime detection

**File:** `week-01/prime-finder/prime_finder.py`

## 🚀 How to Run

### Clone the Repository
```bash
git clone https://github.com/YavuzYaman217/algorithm-design-assignment.git
cd "Algorithm and Analysis"
```

### Run Individual Implementations
```bash
# Run nearest square finder
python week-01/nearest-square/nearest_square.py

# Run prime finder
python week-01/prime-finder/prime_finder.py
```

### Run with Test Framework
```python
# Create a test script or use Python interactively
from test_wrapper import TestWrapper
from week_01.nearest_square.nearest_square import nearest_square

wrapper = TestWrapper(nearest_square, "week-01/nearest-square/test_cases.txt")
wrapper.run_all_tests()
```

## 🛠️ Requirements

- Python 3.7 or higher
- No external dependencies (uses only standard library)

## 📊 Testing

All implementations include comprehensive test cases covering:
- ✅ Normal cases
- ✅ Edge cases (small numbers, perfect squares, etc.)
- ✅ Boundary conditions
- ✅ Performance benchmarks

## 📖 Learning Objectives

Through these projects, students will:
1. Design efficient algorithms for common problems
2. Analyze time and space complexity
3. Write clean, documented code
4. Create comprehensive test cases
5. Apply algorithmic thinking to real-world problems

## 🤝 Contributing

This is a course project repository. If you are a fellow student or instructor and find issues or have suggestions:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is created for educational purposes as part of the Algorithm Design and Analysis course.

## 👤 Author

**Yavuz Yaman**
- GitHub: [@YavuzYaman217](https://github.com/YavuzYaman217)

---

**Note:** This repository will be updated weekly with new assignments and implementations throughout the semester.
