import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

change_dir = (0, 1, 3, 2, 0)
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
sx, sy, sd = map(int, input().split())
sx, sy, sd = sx - 1, sy - 1, change_dir[sd]
ex, ey, ed = map(int, input().split())
ex, ey, ed = ex - 1, ey - 1, change_dir[ed]
dist = [[[-1] * 4 for _ in range(M)] for _ in range(N)]
dist[sx][sy][sd] = 0
q = deque([(sx, sy, sd)])
while q:
    x, y, d = q.popleft()
    if (x, y, d) == (ex, ey, ed):
        break
    for i in range(1, 4):
        nx, ny = x + dx[d] * i, y + dy[d] * i
        if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 0:
            if dist[nx][ny][d] == -1:
                dist[nx][ny][d] = dist[x][y][d] + 1
                q.append((nx, ny, d))
        else:
            break
    for i in (1, -1):
        nd = (d + i) % 4
        if dist[x][y][nd] == -1:
            dist[x][y][nd] = dist[x][y][d] + 1
            q.append((x, y, nd))

print(dist[ex][ey][ed])
