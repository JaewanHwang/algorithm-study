import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline


class Shark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2
        self.exp = 0


def simulate():
    global ans
    q = deque([(shark.x, shark.y)])
    candidates = []
    d = [[-1] * N for _ in range(N)]
    d[shark.x][shark.y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and d[nx][ny] == -1 and m[nx][ny] <= shark.size:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
                if 1 <= m[nx][ny] <= 6 and shark.size > m[nx][ny]:
                    candidates.append((d[nx][ny], nx, ny))
    if not candidates:
        return False
    _, tx, ty = min(candidates)
    ans += d[tx][ty]
    shark.exp += 1
    if shark.exp == shark.size:
        shark.exp = 0
        shark.size += 1
    shark.x, shark.y = tx, ty
    m[tx][ty] = 0
    return True


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

for x in range(N):
    for y in range(N):
        if m[x][y] == 9:
            shark = Shark(x, y)
            m[x][y] = 0
            break

ans = 0
while True:
    if not simulate():
        break
print(ans)
