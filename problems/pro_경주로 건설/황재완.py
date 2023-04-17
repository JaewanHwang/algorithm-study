# 풀이1 dfs
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
ans, cost, N, m = float('inf'), None, None, None


def go(x, y, d):
    global ans
    if x == N - 1 and y == N - 1:
        ans = min(ans, cost[x][y])
        return
    for nd in range(4):
        nx, ny = x + dx[nd], y + dy[nd]
        new_cost = cost[x][y] + (100 if d == nd else 600)
        if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0 and (cost[nx][ny] == -1 or new_cost <= cost[nx][ny]):
            cost[nx][ny] = new_cost
            go(nx, ny, nd)


def solution(board):
    global cost, N, m
    m = board
    N = len(m)
    cost = [[-1] * N for _ in range(N)]
    cost[0][0] = 0
    go(0, 0, 0)
    go(0, 0, 1)
    return ans

#----------------------------------------------------

# 풀이2 bfs
from collections import deque

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)


def solution(board):
    m = board
    N = len(m)
    cost = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
    for d in range(4):
        cost[0][0][d] = 0
    q = deque([[0, 0, 0], [0, 0, 1]])
    while q:
        x, y, d = q.popleft()
        for nd in range(4):
            nx, ny = x + dx[nd], y + dy[nd]
            new_cost = cost[x][y][d] + (100 if d == nd else 600)
            if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0 and (
                    cost[nx][ny][nd] == -1 or cost[nx][ny][nd] > new_cost):
                cost[nx][ny][nd] = new_cost
                q.append((nx, ny, nd))
    ans = min(filter(lambda x: x >= 0, cost[N - 1][N - 1]))
    return ans
