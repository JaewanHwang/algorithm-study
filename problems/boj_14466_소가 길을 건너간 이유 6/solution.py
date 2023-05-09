import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, K, R = map(int, input().split())
path = [[[[False] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
for _ in range(R):
    sr, sc, er, ec = map(lambda x: int(x) - 1, input().split())
    path[sr][sc][er][ec] = path[er][ec][sr][sc] = True

m = [[-1] * N for _ in range(N)]
all_pairs = set((i, j) for i in range(K) for j in range(i + 1, K))
cows = []
for i in range(K):
    x, y = map(lambda x: int(x) - 1, input().split())
    m[x][y] = i
    cows.append((x, y))

for ci, (sx, sy) in enumerate(cows):
    q = deque([(sx, sy)])
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        pair = tuple(sorted([ci, m[x][y]]))
        if m[x][y] != -1 and pair in all_pairs:
            all_pairs.remove(pair)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] or path[x][y][nx][ny]:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))

print(len(all_pairs))
