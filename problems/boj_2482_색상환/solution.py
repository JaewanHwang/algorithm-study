import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
K = int(input())
MOD = 1_000_000_003
dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(N)]
dp[0][0][0] = 1
dp[1][1][1] = 1
dp[1][0][0] = 1
for i in range(2, N - 1):
    for k in range(K + 1):
        dp[i][0][k] = dp[i - 1][0][k] + (dp[i - 1][1][k] if k >= 1 else 0)
        dp[i][1][k] = dp[i - 1][0][k - 1] if k >= 1 else 0

dp[N - 1][0][K] = dp[N - 2][0][K] + dp[N - 2][1][K]
dp[N - 1][1][K] = dp[N - 2][0][K - 1]
res1 = dp[N - 1][0][K] + dp[N - 1][1][K]

dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(N)]
dp[0][1][1] = 1
dp[1][0][1] = 1
for i in range(2, N - 1):
    for k in range(K + 1):
        dp[i][0][k] = dp[i - 1][0][k] + (dp[i - 1][1][k] if k >= 1 else 0)
        dp[i][1][k] = dp[i - 1][0][k - 1] if k >= 1 else 0

dp[N - 1][0][K] = dp[N - 2][0][K] + dp[N - 2][1][K]
res2 = dp[N - 1][0][K]

print((res1 + res2) % MOD)
