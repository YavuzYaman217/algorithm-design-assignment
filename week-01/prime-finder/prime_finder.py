import math
def  prime_finder(n:int) -> list[int]:
    if n < 2:
        return []

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    return primes


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')
    from test_wrapper import TestWrapper
    
    # Test mode
    wrapper = TestWrapper(
        function=prime_finder,
        test_file="test_cases.txt"
    )
    wrapper.run_all_tests()