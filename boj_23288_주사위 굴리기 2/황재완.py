import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]
dice = [0, 0, 0, list(range(7))]
counter_map = {0: 2, 2: 0, 1: 3, 3: 1}


def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    group = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == m[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                group.append((nx, ny))
                q.append((nx, ny))
    for x, y in group:
        dist[x][y] = len(group)


def simulate():
    global ans, dice
    x, y, d, p = dice
    nx, ny = x + dx[d], y + dy[d]
    nd = d
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nd = counter_map[d]
        nx, ny = x + dx[nd], y + dy[nd]
    if nd == 0:
        p[4], p[1], p[3], p[6] = p[6], p[4], p[1], p[3]
    elif nd == 1:
        p[2], p[1], p[5], p[6] = p[6], p[2], p[1], p[5]
    elif nd == 2:
        p[4], p[1], p[3], p[6] = p[1], p[3], p[6], p[4]
    else:
        p[2], p[1], p[5], p[6] = p[1], p[5], p[6], p[2]

    ans += m[nx][ny] * dist[nx][ny]

    A, B = p[6], m[nx][ny]
    if A > B:
        nd = (nd + 1) % 4
    elif A < B:
        nd = (nd - 1) % 4
    dice = [nx, ny, nd, p]


visited = [[False] * M for _ in range(N)]
for x in range(N):
    for y in range(M):
        if not visited[x][y]:
            bfs(x, y)

ans = 0
for _ in range(K):
    simulate()
print(ans)
