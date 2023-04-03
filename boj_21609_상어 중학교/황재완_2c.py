import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def bfs(sx, sy, visited, candidates):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    group = [(sx, sy)]
    rainbow_blocks = []
    base_x, base_y = sx, sy
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and (m[sx][sy] == m[nx][ny] or m[nx][ny] == 0):
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    group.append((nx, ny))
                    if m[nx][ny] == 0:
                        rainbow_blocks.append((nx, ny))
                    else:
                        base_x, base_y = min((nx, ny), (base_x, base_y))
    if len(group) >= 2:
        candidates.append((group, len(rainbow_blocks), base_x, base_y))
    for x, y in rainbow_blocks:
        visited[x][y] = False


def down():
    for y in range(N):
        last_x = N - 1
        for x in range(N - 1, -1, -1):
            if m[x][y] == -2:
                continue
            elif m[x][y] == -1:
                last_x = x - 1
            else:
                tmp = m[x][y]
                m[x][y] = -2
                m[last_x][y] = tmp
                last_x -= 1


def rotate():
    global m
    tm = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            tm[x][y] = m[y][N - 1 - x]
    m = tm


def simulate():
    global ans
    visited = [[False] * N for _ in range(N)]
    candidates = []
    for x in range(N):
        for y in range(N):
            if m[x][y] > 0 and not visited[x][y]:
                bfs(x, y, visited, candidates)
    if not candidates:
        return False
    max_block, _, _, _, = max(candidates, key=lambda x: (len(x[0]), x[1], x[2], x[3]))
    ans += len(max_block) ** 2
    for x, y in max_block:
        m[x][y] = -2
    down()
    rotate()
    down()
    return True


while True:
    if not simulate():
        break
print(ans)
