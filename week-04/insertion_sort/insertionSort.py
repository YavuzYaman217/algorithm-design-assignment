def instertion_sort(arr):
    
    for i in range(2,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
        
    return arr

print(instertion_sort([1,5,0,1]))