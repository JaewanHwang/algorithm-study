import sys

sys.stdin = open('input.txt')


def go(n):
    if dp[n] != -1:
        return dp[n]
    dp[n] = go(n - 1) + go(n - 5)
    return dp[n]


T = int(input())
line = [int(input()) for _ in range(T)]
dp = [-1] * (max(line) + 1)
dp[1:4] = [1] * 3
dp[4:6] = [2] * 2
go(max(line))
for n in line:
    print(dp[n])
