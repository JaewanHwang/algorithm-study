import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [(i, *map(int, input().split())) for i in range(1, N + 1)]
arr.sort(key=lambda x: x[1])
dp = [0] * N
dp[0] = arr[0][2]
h = [i for i in range(N)]
for i in range(1, N):
    max_height = 0
    for j in range(i):
        if arr[j][3] < arr[i][3] and max_height < dp[j]:
            max_height = dp[j]
            h[i] = j
    dp[i] = max_height + arr[i][2]

ans = []
now = dp.index(max(dp))
ans.append(arr[now][0])
while now != h[now]:
    now = h[now]
    ans.append(arr[now][0])
print(len(ans), *ans[::-1], sep='\n')
