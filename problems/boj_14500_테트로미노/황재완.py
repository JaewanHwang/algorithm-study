import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
ans = -1
c = [[False] * M for _ in range(N)]


def go1(x, y, tot, cnt):
    global ans
    if cnt == 4:
        ans = max(ans, tot)
        return
    for i in range(1, 4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not c[nx][ny]:
            c[nx][ny] = True
            go1(nx, ny, tot + m[nx][ny], cnt + 1)
            c[nx][ny] = False


def go2(x, y):
    global ans
    for i in range(4):
        tot = m[x][y]
        for j in range(3):
            nx, ny = x + dx[(i + j) % 4], y + dy[(i + j) % 4]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            tot += m[nx][ny]
        else:
            ans = max(ans, tot)


for x in range(N):
    for y in range(M):
        c[x][y] = True
        go1(x, y, m[x][y], 1)
        c[x][y] = False
        go2(x, y)


print(ans)
