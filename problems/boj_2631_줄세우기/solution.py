import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
a = [int(input()) for _ in range(N)]

dp = [0] * N
dp[0] = 1
for i in range(1, N):
    max_lis = 0
    for j in range(i):
        if a[i] > a[j]:
            max_lis = max(max_lis, dp[j])
    dp[i] = max_lis + 1

ans = N - max(dp)
print(ans)
