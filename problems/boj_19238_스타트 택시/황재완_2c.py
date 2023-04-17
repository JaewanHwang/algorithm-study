import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M, fuel = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(lambda x: int(x) - 1, input().split())
clients = {i: list(map(lambda x: int(x) - 1, input().split())) for i in range(M)}
d = [[[[-1] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
for sx in range(N):
    for sy in range(N):
        if m[sx][sy] == 1:
            continue
        q = deque([(sx, sy)])
        d[sx][sy][sx][sy] = 0
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0 and d[sx][sy][nx][ny] == -1:
                    d[sx][sy][nx][ny] = d[sx][sy][x][y] + 1
                    q.append((nx, ny))


def simulate():
    global tx, ty, fuel
    candidates = []
    for c, (sx, sy, gx, gy) in clients.items():
        if d[tx][ty][sx][sy] >= 0:
            candidates.append((d[tx][ty][sx][sy], sx, sy, c))
    if not candidates:
        return False
    _, _, _, c, = min(candidates)
    sx, sy, gx, gy = clients.pop(c)
    if d[sx][sy][gx][gy] >= 0 and d[tx][ty][sx][sy] + d[sx][sy][gx][gy] <= fuel:
        fuel += d[sx][sy][gx][gy] - d[tx][ty][sx][sy]
        tx, ty = gx, gy
        return True
    return False


for _ in range(M):
    if not simulate():
        fuel = -1
        break
print(fuel)
