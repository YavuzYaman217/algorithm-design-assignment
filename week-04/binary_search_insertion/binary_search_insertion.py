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


a = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
print(insertion_sort(a))
