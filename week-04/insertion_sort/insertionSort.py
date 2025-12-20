def instertion_sort(arr):
    
    for i in range(2,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
        
    return arr

# Test Case 1: Small unsorted array
print(f"Test 1: {instertion_sort([1, 5, 0, 1])} (Expected: [0, 1, 1, 5])")

# Test Case 2: Already sorted
print(f"Test 2: {instertion_sort([1, 2, 3, 4, 5])} (Expected: [1, 2, 3, 4, 5])")

# Test Case 3: Reverse sorted
print(f"Test 3: {instertion_sort([5, 4, 3, 2, 1])} (Expected: [1, 2, 3, 4, 5])")

# Test Case 4: Array with duplicates
print(f"Test 4: {instertion_sort([3, 3, 1, 2, 3, 1])} (Expected: [1, 1, 2, 3, 3, 3])")

# Test Case 5: Single element
print(f"Test 5: {instertion_sort([42])} (Expected: [42])")

# Test Case 6: Two elements
print(f"Test 6: {instertion_sort([2, 1])} (Expected: [1, 2])")

# Test Case 7: Negative numbers
print(f"Test 7: {instertion_sort([-5, 3, -2, 8, -10])} (Expected: [-10, -5, -2, 3, 8])")

# Test Case 8: Mixed positive and negative
print(f"Test 8: {instertion_sort([0, -1, 5, -3, 2])} (Expected: [-3, -1, 0, 2, 5])")

# Test Case 9: All same elements
print(f"Test 9: {instertion_sort([7, 7, 7, 7])} (Expected: [7, 7, 7, 7])")

# Test Case 10: Large random array
print(f"Test 10: {instertion_sort([64, 34, 25, 12, 22, 11, 90])} (Expected: [11, 12, 22, 25, 34, 64, 90])")