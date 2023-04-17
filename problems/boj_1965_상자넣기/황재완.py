import sys

sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    dp[i] = 1
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
