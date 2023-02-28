import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def simulate(di, si):
    global cloud, A
    new_cloud = set()
    for x, y in cloud:
        nx, ny = (x + si * dx[di]) % N, (y + si * dy[di]) % N
        A[nx][ny] += 1
        new_cloud.add((nx, ny))
    tA = [row[:] for row in A]
    for x, y in new_cloud:
        for i in range(1, 8, 2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                tA[x][y] += 1
    A = tA
    cloud = set((x, y) for x in range(N) for y in range(N) if A[x][y] >= 2) - new_cloud
    for x, y in cloud:
        A[x][y] -= 2


cloud = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}
for _ in range(M):
    di, si = map(int, input().split())
    simulate(di - 1, si)
ans = sum(sum(row) for row in A)
print(ans)
