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
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
dx, dy = (1, 0, 0, -1), (0, -1, 1, 0)
dir_to_op = ['d', 'l', 'r', 'u']


def go(x, y, d, k, board, ans, visited, n, m):
    visited[x][y][d] = True
    if board[x][y] == 'E' and d == k:
        return True
    if d == k:
        return False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][d + 1]:
            ans[d] = dir_to_op[i]
            if go(nx, ny, d + 1, k, board, ans, visited, n, m):
                return True
    return False


def solution(n, m, x, y, r, c, k):
    sx, sy, ex, ey = x - 1, y - 1, r - 1, c - 1
    visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
    board = [['.'] * m for _ in range(n)]
    board[ex][ey], board[sx][sy] = 'E', 'S'
    ans = [0] * k
    go(sx, sy, 0, k, board, ans, visited, n, m)
    if not visited[ex][ey][k]:
        return 'impossible'
    ans = ''.join(ans)
    return ans
