def GCD(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# Test Case 1: Co-prime numbers
print(f"Test 1 - GCD(12, 7): {GCD(12, 7)} (Expected: 1)")

# Test Case 2: One divides the other
print(f"Test 2 - GCD(20, 5): {GCD(20, 5)} (Expected: 5)")

# Test Case 3: Same numbers
print(f"Test 3 - GCD(15, 15): {GCD(15, 15)} (Expected: 15)")

# Test Case 4: Large numbers with common factor
print(f"Test 4 - GCD(48, 18): {GCD(48, 18)} (Expected: 6)")

# Test Case 5: One number is zero
print(f"Test 5 - GCD(42, 0): {GCD(42, 0)} (Expected: 42)")

# Test Case 6: Prime numbers
print(f"Test 6 - GCD(17, 19): {GCD(17, 19)} (Expected: 1)")

# Test Case 7: Powers of 2
print(f"Test 7 - GCD(64, 32): {GCD(64, 32)} (Expected: 32)")

# Test Case 8: Fibonacci numbers
print(f"Test 8 - GCD(89, 55): {GCD(89, 55)} (Expected: 1)")

# Test Case 9: Large GCD
print(f"Test 9 - GCD(1071, 462): {GCD(1071, 462)} (Expected: 21)")

# Test Case 10: Consecutive numbers
print(f"Test 10 - GCD(100, 99): {GCD(100, 99)} (Expected: 1)")