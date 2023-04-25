import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(lambda x: int(x), input().split())))
arr.sort(key=lambda x: x[0])
arr = list(map(lambda x: x[1], arr))
dp = [0] * N
dp[0] = 1
for i in range(1, N):
    max_l = 0
    for j in range(i):
        if arr[i] > arr[j]:
            max_l = max(max_l, dp[j])
    dp[i] = max_l + 1
ans = N - max(dp)
print(ans)
