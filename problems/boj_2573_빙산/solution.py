import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

t = 1
found = True
while found:
    tm = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if m[x][y] == 0:
                continue
            cnt = 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 0:
                    cnt += 1
            tm[x][y] = max(0, m[x][y] - cnt)
    m = tm
    visited = [[False] * M for _ in range(N)]
    found = False
    for x in range(N):
        for y in range(M):
            if m[x][y] == 0 or visited[x][y]:
                continue
            if found:
                print(t)
                sys.exit(0)
            found = True
            bfs(x, y)
    t += 1

print(0)
