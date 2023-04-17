import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 0, 0, 1), (0, -1, 1, 0)
change_dir = {1: 0, 2: 3, 3: 2, 4: 1}
R, C, M = map(int, input().split())
m = [[0] * C for _ in range(R)]
sharks = set()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c, d = r - 1, c - 1, change_dir[d]
    s = s % ((2 * C - 2) if 1 <= d <= 2 else (2 * R - 2))
    m[r][c] = (s, d, z)
    sharks.add((r, c, s, d, z))


def simulate(c):
    global ans, m, sharks
    for x in range(R):
        if m[x][c]:
            ans += m[x][c][2]
            sharks.remove((x, c, *m[x][c]))
            m[x][c] = 0
            break

    tm = [[0] * C for _ in range(R)]
    new_sharks = set()
    for x, y, s, d, z in sharks:
        for _ in range(s):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                d = 3 - d
                nx, ny = x + dx[d], y + dy[d]
            x, y = nx, ny
        if tm[x][y]:
            if tm[x][y][2] < z:
                new_sharks.remove((x, y, *tm[x][y]))
                tm[x][y] = (s, d, z)
                new_sharks.add((x, y, s, d, z))
        else:
            tm[x][y] = (s, d, z)
            new_sharks.add((x, y, s, d, z))

    m, sharks = tm, new_sharks


ans = 0
for c in range(C):
    simulate(c)
print(ans)
