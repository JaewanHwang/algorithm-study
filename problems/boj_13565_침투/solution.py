import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
M, N = map(int, input().split())
m = [list(map(int, input().rstrip())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        if x == M - 1:
            return True
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and m[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    return False


for y in range(N):
    if m[0][y] == 0 and not visited[0][y]:
        if bfs(0, y):
            print('YES')
            sys.exit(0)
print('NO')
