import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

used = [[False] * M for _ in range(N)]
ans = 0


def go(i, tot):
    global ans
    if i == N * M:
        ans = max(ans, tot)
        return
    go(i + 1, tot)
    x, y = i // M, i % M
    if used[x][y]:
        return
    for k in range(4):
        ok = True
        branch = []
        for j in range(2):
            nx, ny = x + dx[(k + j) % 4], y + dy[(k + j) % 4]
            if not (0 <= nx < N and 0 <= ny < M and not used[nx][ny]):
                ok = False
                break
            branch.append((nx, ny))
        if ok:
            add = 2 * m[x][y]
            used[x][y] = True
            for nx, ny in branch:
                used[nx][ny] = True
                add += m[nx][ny]
            go(i + 1, tot + add)
            used[x][y] = False
            for nx, ny in branch:
                used[nx][ny] = False


go(0, 0)
print(ans)
