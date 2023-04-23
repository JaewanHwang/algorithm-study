import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
s = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    sx, sy, tx, ty = map(lambda x: int(x) - 1, input().split())
    s[sx][sy].append((tx, ty))
visited = [[False] * N for _ in range(N)]
on = [[False] * N for _ in range(N)]
on[0][0] = True
q = deque([(0, 0)])
visited[0][0] = True
candidates = set()
while q:
    x, y = q.popleft()
    for nx, ny in s[x][y]:
        on[nx][ny] = True
        if (nx, ny) in candidates:
            candidates.remove((nx, ny))
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if on[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
            else:
                candidates.add((nx, ny))

ans = sum(sum(row) for row in on)
print(ans)
