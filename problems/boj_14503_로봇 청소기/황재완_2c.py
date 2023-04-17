import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
N, M = map(int, input().split())
x, y, d = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]


def go(x, y, d):
    if m[x][y] == 0:
        m[x][y] = 2

    blank_exists = False
    for k in range(4):
        nd = (d - k) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 0:
            blank_exists = True
            break
    nd = (d - 1) % 4
    if blank_exists:
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 0:
            go(nx, ny, nd)
        else:
            go(x, y, nd)
    else:
        nx, ny = x - dx[d], y - dy[d]
        if 0 <= nx < N and 0 <= ny < M and m[nx][ny] != 1:
            go(nx, ny, d)


go(x, y, d)
ans = 0
for x in range(N):
    for y in range(M):
        if m[x][y] == 2:
            ans += 1
print(ans)
