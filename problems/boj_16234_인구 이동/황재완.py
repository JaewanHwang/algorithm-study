import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def bfs(x, y):
    q = deque([(x, y)])
    d[x][y] = group
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and L <= abs(A[nx][ny] - A[x][y]) <= R and d[nx][ny] == -1:
                q.append((nx, ny))
                d[nx][ny] = group

ans = 0
while True:
    group = 0
    d = [[-1] * N for _ in range(N)]
    stopped = True
    for x in range(N):
        for y in range(N):
            if d[x][y] == -1:
                bfs(x, y)
                group += 1
    if group == N * N:
        break
    group_population = [[0, 0] for _ in range(group)]
    for x in range(N):
        for y in range(N):
            group_population[d[x][y]][0] += A[x][y]
            group_population[d[x][y]][1] += 1

    group_population = list(map(lambda x: x[0] // x[1], group_population))
    for x in range(N):
        for y in range(N):
            A[x][y] = group_population[d[x][y]]
    ans += 1

print(ans)
