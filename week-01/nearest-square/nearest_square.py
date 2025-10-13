def nearest_square(n: int) -> int: 
    if n < 0:
        return 0

    lower_root = n**0.5
    lower_square = int(lower_root) * int(lower_root)
    upper_root = lower_root + 1
    upper_square = int(upper_root) * int(upper_root)

    if (n - lower_square) <= (upper_square - n):
        return lower_square
    else:
        return upper_square


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')
    from test_wrapper import TestWrapper
    
    # Test mode
    wrapper = TestWrapper(
        function=nearest_square,
        test_file="test_cases.txt"
    )
    wrapper.run_all_tests()