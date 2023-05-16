import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(input().rstrip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
ans = {'W': 0, 'B': 0}


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and m[sx][sy] == m[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    ans[m[sx][sy]] += cnt * cnt


for x in range(M):
    for y in range(N):
        if not visited[x][y]:
            bfs(x, y)
print(ans['W'], ans['B'])
