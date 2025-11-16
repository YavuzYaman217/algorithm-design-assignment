def selection_sort(arr: list) -> list:
    A = arr.copy()
    for i in range(len(A)-1):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')
    from test_wrapper import TestWrapper
    
    wrapper = TestWrapper(
        function=selection_sort,
        test_file="test_cases.txt"
    )
    wrapper.run_all_tests()