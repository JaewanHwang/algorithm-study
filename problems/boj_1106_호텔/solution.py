import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

C, N = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
dp = [float('inf')] * (C + 1)
dp[0] = 0
for i in range(0, C + 1):
    for j in range(N):
        target = min(i + m[j][1], C)
        dp[target] = min(dp[target], dp[i] + m[j][0])

print(dp[C])
