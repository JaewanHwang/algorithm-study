import sys
from collections import deque

sys.stdin = open('input.txt')

R, C, K = map(int, input().split())
heaters = []
check_cells = []
dx, dy = (0, 1, 1, 1, 0, -1, -1, -1), (1, 1, 0, -1, -1, -1, 0, 1)
change_dir = [0, 0, 4, 6, 2]
m = [[0] * C for _ in range(R)]
for r in range(R):
    for c, val in enumerate(map(int, input().split())):
        if 1 <= val <= 4:
            heaters.append((r, c, change_dir[val]))
        elif val == 5:
            check_cells.append((r, c))
W = int(input())
w = [[[[False] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        w[x][y][x - 1][y] = w[x - 1][y][x][y] = True
    else:
        w[x][y][x][y + 1] = w[x][y + 1][x][y] = True


def simulate():
    global m
    for hx, hy, d in heaters:
        x, y = hx + dx[d], hy + dy[d]
        visited = [[-1] * C for _ in range(R)]
        visited[x][y] = 5
        m[x][y] += 5
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            if visited[x][y] == 1:
                continue
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == -1 and not w[x][y][nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] - 1
                m[nx][ny] += visited[nx][ny]

            nx, ny = x + dx[(d - 1) % 8], y + dy[(d - 1) % 8]
            mx, my = x + dx[(d - 2) % 8], y + dy[(d - 2) % 8]
            if 0 <= nx < R and 0 <= ny < C and not w[x][y][mx][my] and not w[mx][my][nx][ny] and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] - 1
                m[nx][ny] += visited[nx][ny]

            nx, ny = x + dx[(d + 1) % 8], y + dy[(d + 1) % 8]
            mx, my = x + dx[(d + 2) % 8], y + dy[(d + 2) % 8]
            if 0 <= nx < R and 0 <= ny < C and not w[x][y][mx][my] and not w[mx][my][nx][ny] and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] - 1
                m[nx][ny] += visited[nx][ny]

    tm = [row[:] for row in m]
    for x in range(R):
        for y in range(C):
            for k in range(0, 7, 2):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < R and 0 <= ny < C and not w[x][y][nx][ny]:
                    diff = m[x][y] - m[nx][ny]
                    if diff > 0:
                        tm[x][y] -= diff // 4
                        tm[nx][ny] += diff // 4
    m = tm
    for y in range(C):
        for x in (0, R - 1):
            if m[x][y] >= 1:
                m[x][y] -= 1
    for x in range(1, R - 1):
        for y in (0, C - 1):
            if m[x][y] >= 1:
                m[x][y] -= 1

    for x, y in check_cells:
        if m[x][y] < K:
            return False
    return True


for ans in range(1, 102):
    if simulate():
        break
print(ans)
