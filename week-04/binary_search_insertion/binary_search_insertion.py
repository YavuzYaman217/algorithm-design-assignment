def binarySearch(arr,item,low,high):
    
    while (low <= high):
        mid = low + (high-low) // 2
        if item == arr[mid]:
            return mid + 1
        if item > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low

def insertion_sort(arr):
    
    for i in range(len(arr)):
        j = i - 1
        key = arr[i]
        loc = binarySearch(arr,key,0,j)
        while (j >= loc):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr


# Test Case 1: Random unsorted array
a = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
print(f"Test 1: {insertion_sort(a.copy())} (Expected: [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100])")

# Test Case 2: Already sorted array
a = [1, 2, 3, 4, 5]
print(f"Test 2: {insertion_sort(a.copy())} (Expected: [1, 2, 3, 4, 5])")

# Test Case 3: Reverse sorted array
a = [5, 4, 3, 2, 1]
print(f"Test 3: {insertion_sort(a.copy())} (Expected: [1, 2, 3, 4, 5])")

# Test Case 4: Array with duplicates
a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Test 4: {insertion_sort(a.copy())} (Expected: [1, 1, 2, 3, 4, 5, 5, 6, 9])")

# Test Case 5: Single element
a = [42]
print(f"Test 5: {insertion_sort(a.copy())} (Expected: [42])")

# Test Case 6: Two elements
a = [2, 1]
print(f"Test 6: {insertion_sort(a.copy())} (Expected: [1, 2])")

# Test Case 7: All same elements
a = [7, 7, 7, 7]
print(f"Test 7: {insertion_sort(a.copy())} (Expected: [7, 7, 7, 7])")

# Test Case 8: Negative numbers
a = [-5, 3, -2, 8, -10, 1]
print(f"Test 8: {insertion_sort(a.copy())} (Expected: [-10, -5, -2, 1, 3, 8])")
