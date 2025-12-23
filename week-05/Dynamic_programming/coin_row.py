def CoinRow(coins):
    n = len(coins)
    if n == 0:
        return 0
    if n == 1:
        return coins[0]
    
    dp = [None] * n
    
    dp[0] = coins[0]
    dp[1] = max(coins[0],coins[1])
    
    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2]+coins[i])
    return dp[n-1]

coins = [5,1,2,10,6,2]
print(CoinRow(coins=coins))
