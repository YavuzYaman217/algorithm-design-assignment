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

print(divide_multiply(15,3))