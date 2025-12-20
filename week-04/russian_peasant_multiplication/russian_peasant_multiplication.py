def divide_multiply(a,b):
    sum = 0
    while b >= 1:
        if (b%2 == 0):
            a = a*2
        else:
            sum += a
            b -=1
        
        b = b // 2
    sum += a
    return sum

# Test Case 1: Example from code
print(f"Test 1 - 15 × 3 = {divide_multiply(15, 3)} (Expected: 45)")

# Test Case 2: Multiply by 1
print(f"Test 2 - 42 × 1 = {divide_multiply(42, 1)} (Expected: 42)")

# Test Case 3: Both numbers small
print(f"Test 3 - 7 × 8 = {divide_multiply(7, 8)} (Expected: 56)")

# Test Case 4: Power of 2
print(f"Test 4 - 16 × 4 = {divide_multiply(16, 4)} (Expected: 64)")

# Test Case 5: Multiply by 2
print(f"Test 5 - 25 × 2 = {divide_multiply(25, 2)} (Expected: 50)")

# Test Case 6: Large numbers
print(f"Test 6 - 123 × 45 = {divide_multiply(123, 45)} (Expected: 5535)")

# Test Case 7: One number is even, one is odd
print(f"Test 7 - 18 × 7 = {divide_multiply(18, 7)} (Expected: 126)")

# Test Case 8: Both numbers odd
print(f"Test 8 - 9 × 11 = {divide_multiply(9, 11)} (Expected: 99)")

# Test Case 9: Small prime numbers
print(f"Test 9 - 13 × 17 = {divide_multiply(13, 17)} (Expected: 221)")

# Test Case 10: Multiplication by power of 2
print(f"Test 10 - 37 × 8 = {divide_multiply(37, 8)} (Expected: 296)")