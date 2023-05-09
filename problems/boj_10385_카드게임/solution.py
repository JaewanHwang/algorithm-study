import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        if a[1][j] < a[0][i]:
            dp[i][j] = max(dp[i][j], dp[i][j + 1] + a[1][j])
        dp[i][j] = max(dp[i][j], dp[i + 1][j + 1])
        dp[i][j] = max(dp[i][j], dp[i + 1][j])

print(dp[0][0])
