
def find_fake_coin_index(arr):
    n = len(arr)
    third = n // 3
    
    group1 = arr[0:third]
    group2 = arr[third:2*third]
    group3 = arr[2*third:]
    
    sum1 = sum(group1)
    sum2 = sum(group2)
    
    if sum1 < sum2:
        fake_index_in_group = group1.index(0)
        return fake_index_in_group
    elif sum2 < sum1:
        fake_index_in_group = group2.index(0)
        return third + fake_index_in_group
    else:
        fake_index_in_group = group3.index(0)
        return 2 * third + fake_index_in_group
    

arr = [1, 1, 1, 1, 1, 0, 1, 1, 1]
fake_coin_pos = find_fake_coin_index(arr)
print(f"The fake coin is at index: {fake_coin_pos}")

arr2 = [1, 1, 1, 1, 0, 1]
fake_coin_pos2 = find_fake_coin_index(arr2)
print(f"The fake coin is at index: {fake_coin_pos2}")


