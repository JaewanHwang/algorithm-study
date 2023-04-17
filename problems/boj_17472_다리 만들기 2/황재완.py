import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
group = 1


def bfs(x, y):
    m[x][y] = group
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == -1:
                m[nx][ny] = group
                q.append((nx, ny))


def find_bridge(m, N, M):
    global x, y
    for x in range(N):
        last, dist = 0, 0
        for y in range(M):
            if m[x][y] == 0:
                dist += 1
            else:
                if last > 0 and dist >= 2:
                    d[last][m[x][y]] = d[m[x][y]][last] = min(d[last][m[x][y]], dist)
                last, dist = m[x][y], 0


def check():
    q = deque([1])
    visited = [False] * group
    cnt = 1
    visited[1] = True
    while q:
        u = q.popleft()
        for v in range(1, group):
            if used[u][v] and not visited[v]:
                visited[v] = True
                q.append(v)
                cnt += 1
    if cnt == group - 1:
        return True
    return False


def go(i, tot):
    global ans
    if tot >= ans:
        return
    if i == len(bridges):
        if check():
            ans = tot
        return
    # 다리를 놓음
    u, v = bridges[i]
    used[u][v] = used[v][u] = True
    go(i + 1, tot + d[u][v])
    # 다리를 놓지 않음
    used[u][v] = used[v][u] = False
    go(i + 1, tot)


for x in range(N):
    for y in range(M):
        if m[x][y] == 1:
            m[x][y] = -1

for x in range(N):
    for y in range(M):
        if m[x][y] == -1:
            bfs(x, y)
            group += 1

d = [[float('inf')] * group for _ in range(group)]
for i in range(1, group):
    d[i][i] = 0
find_bridge(m, N, M)
find_bridge(list(zip(*m)), M, N)

bridges = []
ans = float('inf')
used = [[False] * group for _ in range(group)]
for i in range(1, group):
    for j in range(i + 1, group):
        if d[i][j] != float('inf'):
            bridges.append((i, j))
go(0, 0)
print(ans if ans != float('inf') else -1)
