amount = int(input("Please enter amount of money -> "))
coins = [25,10,5,1]
coins.sort()
result = 0
i = len(coins)-1

while i >= 0 and amount > 0:
    if amount >= coins[i]:
        amount -= coins[i]
        result += 1
    else:
        i -= 1

if amount > 0:
    result = -1

print(result)