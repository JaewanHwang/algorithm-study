import sys
from collections import deque

change = {'.': 0, 'R': 1, 'G': 2, 'B': 3, 'P': 4, 'Y': 5}
sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1),
N, M = 12, 6


def go(sx, sy):
    candidates = [(sx, sy)]
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == m[sx][sy] and not visited[nx][ny]:
                candidates.append((nx, ny))
                q.append((nx, ny))
                visited[nx][ny] = True
    if len(candidates) >= 4:
        for x, y in candidates:
            m[x][y] = 0
        return True
    return False


m = [list(input().rstrip()) for _ in range(N)]
for x in range(N):
    for y in range(M):
        m[x][y] = change[m[x][y]]
ans = 0
for x in range(N):
    if any(m[x]):
        m = m[x:]
        break
while m:
    N = len(m)
    visited = [[False] * M for _ in range(N)]
    removed = False
    for x in range(N):
        for y in range(M):
            if m[x][y] > 0 and not visited[x][y]:
                if go(x, y):
                    removed = True
    if not removed:
        break

    start_x = N
    for y in range(M):
        last_x = N - 1
        for x in range(N - 1, -1, -1):
            if m[x][y] == 0:
                continue
            m[x][y], m[last_x][y] = 0, m[x][y]
            last_x -= 1
        start_x = min(start_x, last_x + 1)
    m = m[start_x:]
    ans += 1

print(ans)
