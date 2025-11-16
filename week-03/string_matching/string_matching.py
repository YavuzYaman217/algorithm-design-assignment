def string_matching(data: list) -> list:
    T, P = data
    n = len(T)
    m = len(P)
    matches = []
    
    if m == 0:
        return matches
    
    for i in range(n - m + 1):
        for j in range(m):
            if T[i+j] != P[j]:
                break
        else:
            matches.append(i)
    
    return matches


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')
    from test_wrapper import TestWrapper
    
    wrapper = TestWrapper(
        function=string_matching,
        test_file="test_cases.txt"
    )
    wrapper.run_all_tests()
