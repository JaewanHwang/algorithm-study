import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)
R, C, T = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R)]
air_cleaner = [0, 0]
for x in range(R):
    if m[x][0] == -1:
        air_cleaner[0] = x
        break


def go(x, y, d, r, prev):
    if m[x][y] == -1:
        return
    cur, m[x][y], nd = m[x][y], prev, d
    nx, ny = x + dx[nd], y + dy[nd]
    if nx < 0 or nx >= R or ny < 0 or ny >= C:
        nd = (nd + 1 * r) % 4
        nx, ny = x + dx[nd], y + dy[nd]
    go(nx, ny, nd, r, cur)


def simulate():
    tm = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if m[x][y] > 0:
                diffuse_amount = m[x][y] // 5
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and m[nx][ny] != -1:
                        tm[nx][ny] += diffuse_amount
                        tm[x][y] -= diffuse_amount
    for x in range(R):
        for y in range(C):
            m[x][y] += tm[x][y]

    ax, ay = air_cleaner
    go(ax, ay + 1, 0, 1, 0)
    go(ax + 1, ay + 1, 0, -1, 0)


for _ in range(T):
    simulate()

ans = sum(sum(filter(lambda x: x > 0, row)) for row in m)
print(ans)
