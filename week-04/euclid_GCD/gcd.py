def GCD(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(GCD(12,7))