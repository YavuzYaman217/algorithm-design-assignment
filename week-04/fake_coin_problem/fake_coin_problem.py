
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
    

# Test Case 1: Fake coin in first group
arr = [0, 1, 1, 1, 1, 1, 1, 1, 1]
print(f"Test 1: {find_fake_coin_index(arr)} (Expected: 0)")

# Test Case 2: Fake coin in second group
arr = [1, 1, 1, 0, 1, 1, 1, 1, 1]
print(f"Test 2: {find_fake_coin_index(arr)} (Expected: 3)")

# Test Case 3: Fake coin in third group
arr = [1, 1, 1, 1, 1, 0, 1, 1, 1]
print(f"Test 3: {find_fake_coin_index(arr)} (Expected: 5)")

# Test Case 4: Small array - fake in first position
arr = [0, 1, 1]
print(f"Test 4: {find_fake_coin_index(arr)} (Expected: 0)")

# Test Case 5: Small array - fake in middle
arr = [1, 0, 1]
print(f"Test 5: {find_fake_coin_index(arr)} (Expected: 1)")

# Test Case 6: Small array - fake in last position
arr = [1, 1, 0]
print(f"Test 6: {find_fake_coin_index(arr)} (Expected: 2)")

# Test Case 7: Six coins - fake in second group
arr = [1, 1, 1, 1, 0, 1]
print(f"Test 7: {find_fake_coin_index(arr)} (Expected: 4)")

# Test Case 8: Nine coins - fake at end
arr = [1, 1, 1, 1, 1, 1, 1, 1, 0]
print(f"Test 8: {find_fake_coin_index(arr)} (Expected: 8)")


