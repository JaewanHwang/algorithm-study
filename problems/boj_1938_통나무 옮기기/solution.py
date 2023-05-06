import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N = int(input())
m = [list(input().rstrip()) for _ in range(N)]
start = []
end = []
for x in range(N):
    for y in range(N):
        if m[x][y] == 'B':
            start.append((x, y))
            m[x][y] = 0
        elif m[x][y] == 'E':
            end.append((x, y))
            m[x][y] = 0
        else:
            m[x][y] = int(m[x][y])
start.sort()
end.sort()
sx, sy = start[1]
sd = 0 if start[0][0] == start[1][0] else 1
ex, ey = end[1]
ed = 0 if end[0][0] == end[1][0] else 1

dist = [[[-1] * 2 for _ in range(N)] for _ in range(N)]
dist[sx][sy][sd] = 0
q = deque([(sx, sy, sd)])


def check1(x, y):
    for nx in range(x - 1, x + 2):
        for ny in range(y - 1, y + 2):
            if m[nx][ny] == 1:
                return False
    return True


def check2(x, y, d, k):
    for x, y in [(x, y), (x, y - 1), (x, y + 1)] if d == 0 else [(x, y), (x - 1, y), (x + 1, y)]:
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or m[nx][ny] == 1:
            return False
    return True


while q:
    x, y, d = q.popleft()
    if (x, y, d) == (ex, ey, ed):
        print(dist[x][y][d])
        sys.exit(0)

    if 0 <= x - 1 and x + 1 < N and 0 <= y - 1 and y + 1 < N and check1(x, y) and dist[x][y][1 - d] == -1:
        dist[x][y][1 - d] = dist[x][y][d] + 1
        q.append((x, y, 1 - d))

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if check2(x, y, d, k) and dist[nx][ny][d] == -1:
            dist[nx][ny][d] = dist[x][y][d] + 1
            q.append((nx, ny, d))
print(0)
