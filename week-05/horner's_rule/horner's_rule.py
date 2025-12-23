#poly 2x^4 - x^3 + 3x^2 + x - 5
A = [2,-1,3,1,-5]
n = 3
result = A[0]
for i in range(1,len(A)):
    result = result * n + A[i]
print(result)