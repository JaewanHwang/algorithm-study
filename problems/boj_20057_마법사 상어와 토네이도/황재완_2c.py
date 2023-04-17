import sys

sys.stdin = open('input.txt')

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
dir_map = [[[0, -1, -1, -1, 1, 1, 1, 0, -2, 2], [-1, -1, 0, 1, 1, 0, -1, -2, 0, 0]]]
dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
percentage = [0, 10, 7, 1, 1, 7, 10, 5, 2, 2]
for k in range(1, 4):
    dir_map.append([[-dir_map[-1][1][i] for i in range(10)]] + [[dir_map[-1][0][i] for i in range(10)]])

ans = 0
visited = [[False] * N for _ in range(N)]
x, y, d = N // 2, N // 2 - 1, 0
visited[x][y + 1] = True
while True:
    if x + y < 0:
        break
    visited[x][y] = True
    cur_amount = m[x][y]
    for k in range(1, 10):
        mx, my = x + dir_map[d][0][k], y + dir_map[d][1][k]
        amount = cur_amount * percentage[k] // 100
        if 0 <= mx < N and 0 <= my < N:
            m[mx][my] += amount
        else:
            ans += amount
        m[x][y] -= amount

    alpha_x, alpha_y = x + dir_map[d][0][0], y + dir_map[d][1][0]
    if 0 <= alpha_x < N and 0 <= alpha_y < N:
        m[alpha_x][alpha_y] += m[x][y]
    else:
        ans += m[x][y]
    m[x][y] = 0

    nd = (d + 1) % 4
    nx, ny = x + dx[nd], y + dy[nd]
    if visited[nx][ny]:
        nd = d
        nx, ny = x + dx[nd], y + dy[nd]
    x, y, d = nx, ny, nd
print(ans)
