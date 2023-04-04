import sys

sys.stdin = open('input.txt')
dx, dy = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cloud = set((i, j) for i in range(N - 2, N) for j in range(2))
for _ in range(M):
    di, si = map(int, input().split())
    di -= 1
    rain_cells = set()
    for cx, cy in cloud:
        ncx, ncy = (cx + dx[di] * si) % N, (cy + dy[di] * si) % N
        rain_cells.add((ncx, ncy))
        A[ncx][ncy] += 1
    for x, y in rain_cells:
        for k in range(1, 8, 2):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                A[x][y] += 1
    new_cloud = set()
    for x in range(N):
        for y in range(N):
            if (x, y) not in rain_cells and A[x][y] >= 2:
                new_cloud.add((x, y))
                A[x][y] -= 2
    cloud = new_cloud
ans = sum(sum(row) for row in A)
print(ans)
