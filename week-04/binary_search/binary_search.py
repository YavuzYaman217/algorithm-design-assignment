def binarySearch(arr,key,low,high):
    while (low <= high):
        mid = low + (high-low)//2
        if key == arr[mid]:
            return 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test Case 1: Element exists in middle
arr = [1, 2, 3, 4, 5]
key = 3
res = binarySearch(arr, key, 0, len(arr)-1)
print(f"Test 1 - arr={arr}, key={key}: {res} (Expected: 1)")

# Test Case 2: Element exists at start
arr = [1, 2, 3, 4, 5]
key = 1
res = binarySearch(arr, key, 0, len(arr)-1)
print(f"Test 2 - arr={arr}, key={key}: {res} (Expected: 1)")

# Test Case 3: Element exists at end
arr = [1, 2, 3, 4, 5]
key = 5
res = binarySearch(arr, key, 0, len(arr)-1)
print(f"Test 3 - arr={arr}, key={key}: {res} (Expected: 1)")

# Test Case 4: Element does not exist
arr = [1, 2, 3, 4, 5]
key = 19
res = binarySearch(arr, key, 0, len(arr)-1)
print(f"Test 4 - arr={arr}, key={key}: {res} (Expected: -1)")

# Test Case 5: Element less than smallest
arr = [10, 20, 30, 40, 50]
key = 5
res = binarySearch(arr, key, 0, len(arr)-1)
print(f"Test 5 - arr={arr}, key={key}: {res} (Expected: -1)")

# Test Case 6: Single element array - found
arr = [42]
key = 42
res = binarySearch(arr, key, 0, len(arr)-1)
print(f"Test 6 - arr={arr}, key={key}: {res} (Expected: 1)")

# Test Case 7: Single element array - not found
arr = [42]
key = 10
res = binarySearch(arr, key, 0, len(arr)-1)
print(f"Test 7 - arr={arr}, key={key}: {res} (Expected: -1)")

# Test Case 8: Large sorted array
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
key = 13
res = binarySearch(arr, key, 0, len(arr)-1)
print(f"Test 8 - arr={arr}, key={key}: {res} (Expected: 1)")