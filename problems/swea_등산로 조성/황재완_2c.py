import sys

sys.stdin = open("input.txt", "r")
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(cur, x, y, tot, used):
    global ans
    ans = max(ans, tot)
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if m[nx][ny] >= cur and not used and m[nx][ny] - cur + 1 <= K:
                visited[nx][ny] = True
                go(cur - 1, nx, ny, tot + 1, True)
                visited[nx][ny] = False
            elif m[nx][ny] < cur:
                visited[nx][ny] = True
                go(m[nx][ny], nx, ny, tot + 1, used)
                visited[nx][ny] = False


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    max_height = max(max(row) for row in m)
    visited = [[False] * N for _ in range(N)]
    ans = 0
    for x in range(N):
        for y in range(N):
            if m[x][y] == max_height:
                visited[x][y] = True
                go(m[x][y], x, y, 1, False)
                visited[x][y] = False
    print(f'#{test_case} {ans}')
