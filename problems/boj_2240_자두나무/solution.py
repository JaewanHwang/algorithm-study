import sys

sys.stdin = open('input.txt')

T, W = map(int, input().split())
dp = [[[-float('inf')] * 2 for _ in range(W + 1)] for _ in range(T + 1)]
dp[0][0][0] = 0
for t in range(1, T + 1):
    tree = int(input()) - 1
    for w in range(min(t, W) + 1):
        if tree == 0:
            dp[t][w][0] = max(dp[t - 1][w - 1][1] + 1 if w > 0 else 0, dp[t - 1][w][0] + 1,
                              dp[t - 1][w - 1][0] + 1 if w > 0 else 0)
            dp[t][w][1] = max(dp[t - 1][w - 1][0] if w > 0 else 0, dp[t - 1][w][1])
        else:
            dp[t][w][1] = max(dp[t - 1][w - 1][0] + 1 if w > 0 else 0, dp[t - 1][w][1] + 1,
                              dp[t - 1][w - 1][1] + 1 if w > 0 else 0)
            dp[t][w][0] = max(dp[t - 1][w - 1][1] if w > 0 else 0, dp[t - 1][w][0])
print(max(max(dp[T][w]) for w in range(W + 1)))
