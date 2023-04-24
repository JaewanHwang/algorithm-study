import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N = int(input())
m = [list(map(int, input().rstrip())) for _ in range(N)]
TARGET = (N - 1, N - 1)
q = deque([(0, 0)])
d = [[-1] * N for _ in range(N)]
d[0][0] = 0
while q:
    x, y, = q.popleft()
    if (x, y) == TARGET:
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if m[nx][ny] == 1 and d[nx][ny] == -1:
                d[nx][ny] = d[x][y]
                q.appendleft((nx, ny))
            elif m[nx][ny] == 0 and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

print(d[N - 1][N - 1])
