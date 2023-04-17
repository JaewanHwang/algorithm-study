import sys

sys.stdin = open('input.txt')


def fibonacci(n, i):
    if dp[n][i] != -1:
        return dp[n][i]
    if n == 0:
        dp[0][0] = 1
        dp[0][1] = 0
    elif n == 1:
        dp[1][1] = 1
        dp[1][0] = 0
    else:
        dp[n][i] = fibonacci(n - 1, i) + fibonacci(n - 2, i)
    return dp[n][i]


T = int(input())
line = [int(input()) for _ in range(T)]
dp = [[-1] * 2 for _ in range(max(line) + 1)]
fibonacci(max(line), 0)
fibonacci(max(line), 1)
for n in line:
    print(*dp[n])
