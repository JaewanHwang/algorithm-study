import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
N, M = map(int, input().split())
r = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]


def go(x, y, d):
    m[x][y] = -1
    for i in range(1, 5):
        nd = (d - i) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if m[nx][ny] == 0:
            go(nx, ny, nd)
            return
    nd = (d + 2) % 4
    nx, ny = x + dx[nd], y + dy[nd]
    if m[nx][ny] != 1:
        go(nx, ny, d)


go(*r)

ans = -sum(sum(filter(lambda x: x == -1, row)) for row in m)
print(ans)
