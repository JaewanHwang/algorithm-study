import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    ok = True
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if m[nx][ny] > m[x][y]:
                ok = False
            if m[nx][ny] == m[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return ok


ans = 0
for x in range(N):
    for y in range(M):
        if not visited[x][y]:
            ans += bfs(x, y)
print(ans)
