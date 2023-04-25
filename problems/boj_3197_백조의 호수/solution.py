import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
R, C = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]

q = deque()
d1 = [[-1] * C for _ in range(R)]
player = []
for x in range(R):
    for y in range(C):
        if m[x][y] == '.':
            q.append((x, y))
            d1[x][y] = 0
        elif m[x][y] == 'L':
            player.append((x, y))
            q.append((x, y))
            d1[x][y] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and d1[nx][ny] == -1 and m[nx][ny] == 'X':
            q.append((nx, ny))
            d1[nx][ny] = d1[x][y] + 1

sx, sy = player[0]
ex, ey = player[1]
q = deque([(sx, sy)])
d2 = [[-1] * C for _ in range(R)]
d2[sx][sy] = 0
while q:
    if (x, y) == (ex, ey):
        break
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and d2[nx][ny] == -1:
            if d1[nx][ny] <= d2[x][y]:
                q.appendleft((nx, ny))
                d2[nx][ny] = d2[x][y]
            else:
                q.append((nx, ny))
                d2[nx][ny] = d1[nx][ny]

print(d2[ex][ey])
