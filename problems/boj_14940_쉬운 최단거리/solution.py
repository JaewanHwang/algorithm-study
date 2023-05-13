import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
d = [[-1] * M for _ in range(N)]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    d[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and d[nx][ny] == -1 and m[nx][ny] == 1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
    for x in range(N):
        for y in range(M):
            if m[x][y] == 0:
                d[x][y] = 0
    for row in d:
        print(*row)


for x in range(N):
    for y in range(M):
        if m[x][y] == 2:
            bfs(x, y)
            sys.exit(0)
