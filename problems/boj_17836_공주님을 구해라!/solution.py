import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M, T = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
d = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
d[0][0][0] = 0
q = deque([(0, 0, 0)])
while q:
    x, y, get = q.popleft()
    if (x, y) == (N - 1, M - 1):
        print(d[x][y][get])
        sys.exit(0)
    if d[x][y][get] == T:
        continue
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if m[nx][ny] == 0 and d[nx][ny][get] == -1:
                q.append((nx, ny, get))
                d[nx][ny][get] = d[x][y][get] + 1
            elif m[nx][ny] == 1 and get and d[nx][ny][get] == -1:
                q.append((nx, ny, get))
                d[nx][ny][get] = d[x][y][get] + 1
            elif m[nx][ny] == 2 and d[nx][ny][1] == -1:
                q.append((nx, ny, 1))
                d[nx][ny][1] = d[x][y][get] + 1

print('Fail')
