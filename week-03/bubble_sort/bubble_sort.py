def bubble_sort(arr: list) -> list:
    A = arr.copy()
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')
    from test_wrapper import TestWrapper
    
    wrapper = TestWrapper(
        function=bubble_sort,
        test_file="test_cases.txt"
    )
    wrapper.run_all_tests()