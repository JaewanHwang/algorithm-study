import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
m = [list(input().rstrip()) for _ in range(N)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0


def bfs(x, y):
    global ans
    d = [[-1] * M for _ in range(N)]
    d[x][y] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        ans = max(d[x][y], ans)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 'L' and d[nx][ny] == -1:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1


visited = [[False] * M for _ in range(N)]
for x in range(N):
    for y in range(M):
        if m[x][y] == 'L':
            bfs(x, y)
print(ans)
