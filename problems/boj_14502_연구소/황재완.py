import sys
from collections import deque
from itertools import combinations

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
SAFE_AREA = -3
v = []
wc = []
for x in range(N):
    for y in range(M):
        if m[x][y] == 0:
            SAFE_AREA += 1
            wc.append((x, y))
        elif m[x][y] == 2:
            v.append((x, y))
ans = 0


def go(*walls):
    res = 0
    q = deque(v)
    c = [row[:] for row in m]
    for x, y in walls:
        c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and c[nx][ny] == 0:
                q.append((nx, ny))
                c[nx][ny] = 2
                res += 1
    return res


for w1, w2, w3 in combinations(wc, r=3):
    ans = max(ans, SAFE_AREA - go(w1, w2, w3))


print(ans)
