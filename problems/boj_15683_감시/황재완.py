import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
TBC = 0
cctvs = []
for x in range(N):
    for y in range(M):
        if m[x][y] == 0:
            TBC += 1
        elif 1 <= m[x][y] <= 5:
            cctvs.append([x, y, -1])
num_to_dirs = {1: ((0,), (1,), (2,), (3,)),
               2: ((1, 3), (0, 2)),
               3: ((0, 1), (1, 2), (2, 3), (0, 3)),
               4: ((0, 1, 3), (0, 1, 2), (1, 2, 3), (2, 3, 0)),
               5: ((0, 1, 2, 3),)}


def simulate():
    global ans
    tm = [row[:] for row in m]
    cnt = 0
    for x, y, dirs in cctvs:
        for dir in dirs:
            nx, ny = x + dx[dir], y + dy[dir]
            while 0 <= nx < N and 0 <= ny < M and tm[nx][ny] != 6:
                if tm[nx][ny] == 0:
                    tm[nx][ny] = -1
                    cnt += 1
                nx, ny = nx + dx[dir], ny + dy[dir]
    ans = min(ans, TBC - cnt)


def go(n):
    if n == len(cctvs):
        simulate()
        return
    x, y, _ = cctvs[n]
    for dirs in num_to_dirs[m[x][y]]:
        cctvs[n][2] = dirs
        go(n + 1)


ans = N * M
go(0)

print(ans)
