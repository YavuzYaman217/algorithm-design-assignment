def sequential_search(data: list) -> int:
    arr, key = data
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')
    from test_wrapper import TestWrapper
    
    wrapper = TestWrapper(
        function=sequential_search,
        test_file="test_cases.txt"
    )
    wrapper.run_all_tests()