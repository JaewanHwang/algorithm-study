import sys
from itertools import combinations

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
d = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    d[a][b] = 1
    d[b][a] = 1
for n in range(1, N + 1):
    d[n][n] = 0
for k in range(1, N + 1):
    for u in range(1, N + 1):
        for v in range(1, N + 1):
            d[u][v] = min(d[u][v], d[u][k] + d[k][v])

ans = [0, 0, float('inf')]  # min_x, min_y, min_sum
for x, y in combinations(range(1, N + 1), r=2):
    res = 0
    for n in range(1, N + 1):
        res += 2 * min(d[x][n], d[y][n])
    if ans[2] > res:
        ans[:2] = x, y
        ans[2] = res
print(*ans)
