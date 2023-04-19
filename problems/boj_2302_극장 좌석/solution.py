import sys

sys.stdin = open('input.txt')
N = int(input())
M = int(input())
fix = set(int(input()) for _ in range(M))
dp = [0] * (N + 1)
dp[0] = dp[1] = 1
for i in range(2, N + 1):
    if i in fix:
        dp[i] = dp[i - 1]
    else:
        if i - 1 in fix:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N])
