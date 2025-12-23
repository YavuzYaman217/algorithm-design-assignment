def power(a,b):
    if (b == 0): return 1
    if (b == 1): return a
    temp = power(a,b//2)
    result = temp * temp
    return result if b%2 == 0 else result*a 

print(power(2,6))
    