import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
dirs = [[-2, 0, 2], [-1, -1, 10], [-1, 0, 7], [-1, 1, 1], [0, -2, 5], [1, -1, 10], [1, 0, 7], [1, 1, 1], [2, 0, 2],
        [0, -1, 0]]
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = 0


def go(x, y, d):
    global ans
    visited[x][y] = True
    tot = 0
    for i in range(len(dirs) - 1):
        nx, ny, p = x + dirs[i][0], y + dirs[i][1], dirs[i][2]
        amount = int(p / 100 * m[x][y])
        tot += amount
        if 0 <= nx < N and 0 <= ny < N:
            m[nx][ny] += amount
        else:
            ans += amount

    amount = m[x][y] - tot
    nx, ny = x + dirs[-1][0], y + dirs[-1][1]
    if 0 <= nx < N and 0 <= ny < N:
        m[nx][ny] += amount
    else:
        ans += amount
    if x == 0 and y == 0:
        return
    nx, ny = x + dx[(d + 1) % 4], y + dy[(d + 1) % 4]
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        for i in range(len(dirs)):
            dirs[i][0], dirs[i][1] = -dirs[i][1], dirs[i][0]
        go(nx, ny, (d + 1) % 4)
    else:
        go(x + dx[d], y + dy[d], d)


visited[N // 2][N // 2] = True
go(N // 2, N // 2 - 1, 0)
print(ans)
