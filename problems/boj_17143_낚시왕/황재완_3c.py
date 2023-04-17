import sys

sys.stdin = open('input.txt')

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
change_dir = [0, 3, 1, 0, 2]
R, C, M = map(int, input().split())
m = [[0] * C for _ in range(R)]
sharks = dict()
for si in range(1, M + 1):
    r, c, s, d, z = map(int, input().split())
    r, c, d = r - 1, c - 1, change_dir[d]
    sharks[si] = [r, c, s % (2 * ((C if d == 0 or d == 2 else R) - 2) + 2), d, z]
    m[r][c] = si


def simulate(cur_y):
    global ans, m, sharks
    # 땅과 가장 가까운 상어를 잡는다.
    for x in range(R):
        if m[x][cur_y] > 0:
            ans += sharks[m[x][cur_y]][-1]
            sharks.pop(m[x][cur_y])
            break

    # 상어 이동
    tm = [[0] * C for _ in range(R)]
    tsharks = dict()
    for si in sharks:
        x, y, s, d, z = sharks[si]
        for _ in range(s):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                nd = (d + 2) % 4
                nx, ny = x + dx[nd], y + dy[nd]
            else:
                nd = d
            x, y, d = nx, ny, nd
        if tm[x][y] > 0 and tsharks[tm[x][y]][-1] > z:
            continue
        if tm[x][y] > 0 and tsharks[tm[x][y]][-1] < z:
            tsharks.pop(tm[x][y])
        tm[x][y] = si
        tsharks[si] = [x, y, s, d, z]

    m, sharks = tm, tsharks


ans = 0
for c in range(C):
    simulate(c)
print(ans)
