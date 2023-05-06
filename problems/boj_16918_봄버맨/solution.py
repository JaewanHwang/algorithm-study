import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
R, C, N = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]


def bfs(x, y, t):
    q = deque([(x, y)])
    m[x][y] = t
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and m[nx][ny] == -1:
            m[nx][ny] = t
            q.append((nx, ny))


for x in range(R):
    for y in range(C):
        if m[x][y] == '.':
            m[x][y] = -1
        else:
            m[x][y] = 0

for t in range(2, N + 1):
    removed = []
    for x in range(R):
        for y in range(C):
            if m[x][y] == -1:
                bfs(x, y, t)
            if t - 3 == m[x][y] >= 0:
                removed.append((x, y))
    for x, y in removed:
        m[x][y] = -1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                m[nx][ny] = -1

for row in m:
    print(''.join(map(lambda x: '.' if x == -1 else 'O', row)))
