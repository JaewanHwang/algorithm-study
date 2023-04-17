import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]


class Shark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2
        self.exp = 0


for x in range(N):
    for y in range(N):
        if m[x][y] == 9:
            shark = Shark(x, y)
            m[x][y] = 0
            break

ans = 0
while True:
    d = [[-1] * N for _ in range(N)]
    d[shark.x][shark.y] = 0
    q = deque()
    q.append((shark.x, shark.y))
    candidates = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and d[nx][ny] == -1 and m[nx][ny] <= shark.size:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1
                if 0 < m[nx][ny] < shark.size:
                    candidates.append((d[nx][ny], nx, ny))
    if not candidates:
        break
    dist, nx, ny = min(candidates)
    m[nx][ny] = 0
    shark.x, shark.y = nx, ny
    shark.exp += 1
    if shark.exp == shark.size:
        shark.exp = 0
        shark.size += 1
    ans += dist

print(ans)
