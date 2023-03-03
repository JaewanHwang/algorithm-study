# 풀이 1: BFS + 그리기 + 역추적 기법
from collections import deque

dx, dy = (1, 0, 0, -1), (0, -1, 1, 0)
dir_to_op = ['d', 'l', 'r', 'u']


def bfs(x, y, n, m, d, k):
    d[x][y][0] = (-1, -1, -1)
    q = deque([(x, y, 0)])
    while q:
        x, y, dist = q.popleft()
        if dist == k:
            continue
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and d[nx][ny][dist + 1] == -1:
                d[nx][ny][dist + 1] = (x, y, dir)
                q.append((nx, ny, dist + 1))


def solution(n, m, x, y, r, c, k):
    sx, sy, ex, ey = x - 1, y - 1, r - 1, c - 1
    d = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
    bfs(sx, sy, n, m, d, k)

    if d[ex][ey][k] == -1:
        return 'impossible'
    ans = ''
    x, y, dist = ex, ey, k
    while dist > 0:
        x, y, dir = d[x][y][dist]
        ans += dir_to_op[dir]
        dist -= 1

    return ans[::-1]

# 풀이 2: DFS + 그리디
