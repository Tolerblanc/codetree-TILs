n = int(input())
dp = [0] * 1001

dp[2] = dp[3] = 1
for i in range(4, n):
    dp[i] = dp[i - 2] + dp[i - 3]

print(dp[n])