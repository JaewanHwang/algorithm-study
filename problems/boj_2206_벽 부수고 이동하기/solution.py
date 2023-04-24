import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().rstrip())) for _ in range(N)]
d = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
d[0][0][0] = 0
q = deque([(0, 0, 0)])
TARGET = (N - 1, M - 1)
ans = -1
while q:
    x, y, used = q.popleft()
    if (x, y) == TARGET:
        ans = d[x][y][used] + 1
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if m[nx][ny] == 0:
                if d[nx][ny][used] == -1:
                    d[nx][ny][used] = d[x][y][used] + 1
                    q.append((nx, ny, used))
            else:
                if d[nx][ny][used] == -1 and not used:
                    d[nx][ny][True] = d[x][y][used] + 1
                    q.append((nx, ny, True))

print(ans)
