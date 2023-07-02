# using recursion
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)

# using DP memoization:
def fib2(n,dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib2(n-1, dp) + fib2(n-2, dp)
    return dp[n]

# using DP tabulation:
def fib3(n, dp):
    dp[0] = 0
    dp[1] = 1

    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space Optimization in Tabulation
def fib4(n):
    prev2 = 0
    prev = 1
    for i in range(2,n+1):
        curr = prev2 + prev
        prev2 = prev
        prev = curr
    return prev
    

# Passing Parameters
n = 8
dp = [-1] * (n+1)
print(fib1(n), "Using Recursion")

print(fib2(n,dp) , "Using Memoization")

print(fib3(n, dp) , "Using Tabulation")

print(fib4(n) , "Space Optimization in Tabulation")