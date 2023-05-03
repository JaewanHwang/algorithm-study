import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

N, M, A, B, K = map(int, input().split())
m = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(lambda x: int(x) - 1, input().split())
    m[x][y] = 1
sx, sy = map(lambda x: int(x) - 1, input().split())
ex, ey = map(lambda x: int(x) - 1, input().split())
d = [[-1] * M for _ in range(N)]
d[sx][sy] = 0
q = deque([(sx, sy)])


def make_range(x, y, k):
    if k == 0:
        return range(x, x + 1), range(y, y + B)
    elif k == 1:
        return range(x + A - 1, x + A), range(y, y + B)
    elif k == 2:
        return range(x, x + A), range(y, y + 1)
    else:
        return range(x, x + A), range(y + B - 1, y + B)


def check(x_range, y_range):
    for x in x_range:
        for y in y_range:
            if m[x][y] == 1:
                return False
    return True


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M and 0 <= x + A - 1 < N and 0 <= y + B - 1 < M


while q:
    x, y = q.popleft()
    if (x, y) == (ex, ey):
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if not in_range(nx, ny) or d[nx][ny] != -1:
            continue

        if check(*make_range(nx, ny, k)):
            q.append((nx, ny))
            d[nx][ny] = d[x][y] + 1

print(d[ex][ey])
