def merge(arr,left,mid,right):
    n1 = mid - left + 1
    n2 = right - mid
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[left+i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Test Case 1: Small array
arr = [1, 3, 0, 7]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 1: {arr} (Expected: [0, 1, 3, 7])")

# Test Case 2: Already sorted
arr = [1, 2, 3, 4, 5]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 2: {arr} (Expected: [1, 2, 3, 4, 5])")

# Test Case 3: Reverse sorted
arr = [5, 4, 3, 2, 1]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 3: {arr} (Expected: [1, 2, 3, 4, 5])")

# Test Case 4: Array with duplicates
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 4: {arr} (Expected: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9])")

# Test Case 5: Single element
arr = [42]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 5: {arr} (Expected: [42])")

# Test Case 6: Two elements
arr = [2, 1]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 6: {arr} (Expected: [1, 2])")

# Test Case 7: Power of 2 length
arr = [64, 34, 25, 12, 22, 11, 90, 88]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 7: {arr} (Expected: [11, 12, 22, 25, 34, 64, 88, 90])")

# Test Case 8: Negative numbers
arr = [-5, 3, -2, 8, -10, 1]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 8: {arr} (Expected: [-10, -5, -2, 1, 3, 8])")

# Test Case 9: All same elements
arr = [7, 7, 7, 7, 7]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 9: {arr} (Expected: [7, 7, 7, 7, 7])")

# Test Case 10: Large random array
arr = [38, 27, 43, 3, 9, 82, 10]
mergeSort(arr, 0, len(arr) - 1)
print(f"Test 10: {arr} (Expected: [3, 9, 10, 27, 38, 43, 82])")