fibArray = {}

def fib(n):
    if n in fibArray:
        return fibArray[n]
    if n == 0:
        fibArray[0] = 0
        return 0
    if n == 1:
        fibArray[1] = 1
        return 1
    fibArray[n] = fib(n-1) + fib(n-2)
    return fibArray[n]

print(fib(6))

#The code above the both space and time complexity are linear O(n)

def fib_with_for(n):
    if (n == 0 or n == 1):
        return n
    back1= 1
    back2 = 0
    
    for i in range(2,n+1):
        current = back1 + back2
        back2 = back1
        back1 = current
    return current

print(fib_with_for(6))
#The code above the time complexity is O(n) while space complexity is O(1)
        
    