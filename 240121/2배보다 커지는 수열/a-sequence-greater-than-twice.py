import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(M+1):
    dp[1][i] = i

for i in range(2, N+1):
    for j in range(1, M+1):
        for k in range(1, j//2+1):
            dp[i][j] += dp[i-1][k]

print(sum(dp[N])%1000000007)