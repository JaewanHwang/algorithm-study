import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    x, a = map(int, input().split())
    A.append((x, a))
A.sort()
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + A[i - 1][1]

p = 1
ans = float('inf')
min_diff = float('inf')
visited = [0] * (N + 1)
while True:
    if visited[p]:
        break
    visited[p] = True
    res = abs(s[p - 1] - (s[N] - s[p]))
    if min_diff > res:
        min_diff = res
        ans = A[p - 1][0]
    if s[p - 1] >= s[N] - s[p]:
        p -= 1
    else:
        p += 1
print(ans)
