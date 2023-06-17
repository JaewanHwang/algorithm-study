import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0, -1, -1, 1, 1), (0, 0, -1, 1, -1, 1, 1, -1)
M, N = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
ans = 0


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and m[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True


for x in range(M):
    for y in range(N):
        if m[x][y] == 1 and not visited[x][y]:
            bfs(x, y)
            ans += 1

print(ans)
