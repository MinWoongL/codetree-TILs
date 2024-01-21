import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(M+1):
    dp[1][i] = i

for i in range(2, N+1):
    tmp = 0
    for j in range(1, M+1):
        tmp += dp[i-1][j//2]
        dp[i][j] = (tmp%1000000007)

print(dp[-1][-1])