import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
sx, sy = map(lambda x: int(x) - 1, input().split())
ex, ey = map(lambda x: int(x) - 1, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
d = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
d[sx][sy][False] = 0
q = deque([(sx, sy, 0)])

while q:
    x, y, used = q.popleft()
    if (x, y) == (ex, ey):
        print(d[x][y][used])
        sys.exit(0)
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if m[nx][ny] == 0 and d[nx][ny][used] == -1:
            q.append((nx, ny, used))
            d[nx][ny][used] = d[x][y][used] + 1
        elif m[nx][ny] == 1 and not used and d[nx][ny][True] == -1:
            q.append((nx, ny, True))
            d[nx][ny][True] = d[x][y][used] + 1
print(-1)
