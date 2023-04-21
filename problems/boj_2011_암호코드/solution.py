import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
MOD = 1000000
exp = list(map(int, input().rstrip()))
N = len(exp)
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    if i - 2 >= 0:
        if 10 <= exp[i - 2] * 10 + exp[i - 1] <= 26:
            dp[i] = (dp[i] + dp[i - 2]) % MOD
    if i - 1 >= 0:
        if 1 <= exp[i - 1] <= 9:
            dp[i] = (dp[i] + dp[i - 1]) % MOD

print(dp[N])
