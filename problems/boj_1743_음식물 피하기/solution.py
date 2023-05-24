import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M, K = map(int, input().split())
m = [[False] * M for _ in range(N)]
for _ in range(K):
    x, y = map(lambda x: int(x) - 1, input().split())
    m[x][y] = True


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt


visited = [[False] * M for _ in range(N)]
ans = 0
for x in range(N):
    for y in range(M):
        if m[x][y] and not visited[x][y]:
            ans = max(ans, bfs(x, y))
print(ans)
