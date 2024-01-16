import sys
N = int(input())

dp = [0]*100

dp[0] = 2
dp[1] = 4
for i in range(2, 100):
    dp[i] = (dp[i-1]*dp[i-2])%100

print(dp[N-1])