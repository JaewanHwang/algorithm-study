import sys

sys.setrecursionlimit(10 ** 4)
sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]


def go(x, y, prev, d, rotation):
    if A[x][y] == -1:
        return
    cur = A[x][y]
    A[x][y] = prev
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < R and 0 <= ny < C:
        go(nx, ny, cur, d, rotation)
    else:
        nd = (d + rotation) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        go(nx, ny, cur, nd, rotation)


def simulate():
    tA = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] > 0:
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        diffuse = A[x][y] // 5
                        tA[x][y] -= diffuse
                        tA[nx][ny] += diffuse
    for x in range(R):
        for y in range(C):
            if A[x][y] != -1:
                A[x][y] += tA[x][y]

    go(air_cleaner_x, 1, 0, 0, -1)
    go(air_cleaner_x + 1, 1, 0, 0, 1)


for x in range(R):
    if A[x][0] == -1:
        air_cleaner_x = x
        break

for _ in range(T):
    simulate()

ans = 0
for x in range(R):
    for y in range(C):
        if A[x][y] > 0:
            ans += A[x][y]
print(ans)
