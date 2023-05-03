import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
m = [[0] * M for _ in range(N)]
dx, dy = (-1, -1, 0), (0, -1, -1)
ans = 0


def go(i):
    global ans
    if i == N * M:
        ans += 1
        return
    x, y = i // M, i % M
    cnt = 0
    for k in range(3):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 1:
            cnt += 1
    if cnt < 3:
        m[x][y] = 1
        go(i + 1)

    m[x][y] = 0
    go(i + 1)


go(0)
print(ans)
