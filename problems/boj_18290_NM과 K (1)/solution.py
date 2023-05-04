import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 0), (0, -1)
N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
used = [[False] * M for _ in range(N)]


def check(x, y):
    if used[x][y]:
        return False
    for d in range(2):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and used[nx][ny]:
            return False
    return True


def go(sx, sy, k, tot):
    global ans
    if k == K:
        ans = max(ans, tot)
        return
    for x in range(sx, N):
        for y in range(sy, M):
            if check(x, y):
                used[x][y] = True
                go(x, y, k + 1, tot + m[x][y])
                used[x][y] = False
        sy = 0


ans = -float('inf')
go(0, 0, 0, 0)
print(ans)
