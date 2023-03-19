import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("sample_input.txt", "r")
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(cur_height, x, y, cut, dist):
    global ans
    ans = max(ans, dist)
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny]:
            continue
        if cur_height > m[nx][ny]:
            visited[nx][ny] = True
            go(m[nx][ny], nx, ny, cut, dist + 1)
            visited[nx][ny] = False
        elif cur_height <= m[nx][ny] and not cut and m[nx][ny] - cur_height < K:
            visited[nx][ny] = True
            go(cur_height - 1, nx, ny, True, dist + 1)
            visited[nx][ny] = False


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    max_height = max(max(row) for row in m)
    ans = 0
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if m[x][y] == max_height:
                visited[x][y] = True
                go(m[x][y], x, y, False, 1)
                visited[x][y] = False
    print(f'#{test_case} {ans}')
