#Here is the naive approach.
# O(2^n)
def knapsack_(capacity,v,w,n):
    if n == 0 or capacity == 0:
        return 0
    
    pick = 0
    
    if w[n-1] <= capacity:
        pick = v[n-1] + knapsack_(capacity - w[n-1],v,w,n-1)
    
    notpick = knapsack_(capacity - w[n-1],v,w,n-1)
    
    return max(pick,notpick)

def knapsack(capacity, amount, wt):
    n = len(amount)
    return knapsack_(capacity, amount, wt, n)

#Here is the better approach
# O(n*capacity)

def better_knapsack(capacity,amount,w):
    
    dp = [0] * (capacity+1)
    
    for i in range (1,len(w) + 1):
        for j in range(capacity,w[i-1]-1,-1):
            dp[j] = max(dp[j], dp[j - w[i - 1]] + amount[i - 1])
    return dp[capacity]

    
if __name__ == "__main__":
    amount = [1, 2, 3]
    wt = [4, 5, 1]
    capacity = 6
    print(knapsack(capacity, amount, wt))
    print(better_knapsack(capacity,amount,wt))
    
