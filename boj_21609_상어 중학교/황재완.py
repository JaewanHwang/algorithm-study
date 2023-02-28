import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
RAINBOW = M + 1
m = [list(map(lambda x: int(x) if x != '0' else RAINBOW, input().split())) for _ in range(N)]


def find_biggest_block_group():
    global ans
    visited = [[False] * N for _ in range(N)]
    candidate_list = []
    for x in range(N):
        for y in range(N):
            if 0 < m[x][y] < RAINBOW and not visited[x][y]:
                bfs(x, y, visited, candidate_list)
    if not candidate_list:
        return False
    _, _, _, _, block_group = max(candidate_list)
    ans += len(block_group) ** 2
    for x, y in block_group:
        m[x][y] = 0
    return True


def bfs(sx, sy, visited, candidate_list):
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    rainbow_list = []
    block_group = [(sx, sy)]
    color = m[sx][sy]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and (m[nx][ny] == RAINBOW or m[nx][ny] == color):
                if m[nx][ny] == RAINBOW:
                    rainbow_list.append((nx, ny))
                q.append((nx, ny))
                visited[nx][ny] = True
                block_group.append((nx, ny))

    if len(block_group) >= 2:
        candidate_list.append((len(block_group), len(rainbow_list), sx, sy, block_group))
    for x, y in rainbow_list:
        visited[x][y] = False


def gravity():
    for y in range(N):
        last = N - 1
        for x in range(N - 1, -1, -1):
            if m[x][y] == 0:
                continue
            elif m[x][y] == -1:
                last = x - 1
            else:
                m[x][y], m[last][y] = 0, m[x][y]
                last -= 1


def rotate():
    global m
    tm = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            tm[x][y] = m[y][N - 1 - x]
    m = tm


ans = 0
while True:
    if not find_biggest_block_group():
        break
    gravity()
    rotate()
    gravity()
print(ans)
