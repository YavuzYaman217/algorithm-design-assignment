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

arr = [1,2,3,4,5]
res = binarySearch(arr=arr,key = 19,low=0,high=len(arr)-1)
print(res)