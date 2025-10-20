def locker_problem_slow(door_number: int) -> list[int]:
    doors = [False] * (door_number + 1) 
    
    for i in range(1, door_number + 1):
        for j in range(i, door_number + 1, i):
            doors[j] = not doors[j]
    
    open_lockers = []
    for index, door in enumerate(doors):
        if door:
            open_lockers.append(index)
    return open_lockers


def locker_problem_fast(door_number: int) -> list[int]:
    open_lockers = []
    i = 1
    while i * i <= door_number:
        open_lockers.append(i * i)
        i += 1
    return open_lockers


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')
    from test_wrapper import TestWrapper
    
    print("=" * 80)
    print("LOCKER PROBLEM - PERFORMANCE COMPARISON")
    print("=" * 80)
    
    # Test the slow brute force algorithm
    print("\n1. Testing SLOW Algorithm (Brute Force - O(N log N)):")
    wrapper_slow = TestWrapper(
        function=locker_problem_slow,
        test_file="test_cases.txt"
    )
    wrapper_slow.run_all_tests()
    
    # Test the fast mathematical algorithm  
    print("\n2. Testing FAST Algorithm (Mathematical - O(√N)):")
    wrapper_fast = TestWrapper(
        function=locker_problem_fast,
        test_file="test_cases.txt"
    )
    wrapper_fast.run_all_tests()
    
    # Manual performance comparison for large inputs
    print("\n4. Manual Performance Test for Large Inputs:")
    test_sizes = [100, 1000, 10000]
    
    for size in test_sizes:
        print(f"\nTesting with {size} lockers:")
        
        # Test slow algorithm
        import time
        start_time = time.perf_counter()
        result_slow = locker_problem_slow(size)
        slow_time = (time.perf_counter() - start_time) * 1000
        
        # Test fast algorithm  
        start_time = time.perf_counter()
        result_fast = locker_problem_fast(size)
        fast_time = (time.perf_counter() - start_time) * 1000
        
        # Verify results are the same
        results_match = result_slow == result_fast
        
        print(f"  Slow Algorithm:     {slow_time:.4f}ms")
        print(f"  Fast Algorithm:     {fast_time:.4f}ms") 
        print(f"  Results Match:      {results_match}")
        if slow_time > 0 and fast_time > 0:
            print(f"  Speed Improvement:  {slow_time/fast_time:.2f}x faster")
        print(f"  Open Lockers Count: {len(result_fast)}")
    
    print("\n" + "=" * 80)




