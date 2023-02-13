import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)

R, C, M = map(int, input().split())
m = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    m[r - 1][c - 1].append((s, d - 1, z))


def move(x, y):
    s, d, z = m[x][y].pop()
    period = 2 * (R if 0 <= d <= 1 else C) - 2
    for _ in range(s % period):
        if x + dx[d] < 0 or x + dx[d] >= R or y + dy[d] < 0 or y + dy[d] >= C:
            d = 1 - d if 0 <= d <= 1 else 5 - d
        x, y = x + dx[d], y + dy[d]

    if tm[x][y]:
        os, od, oz = tm[x][y].pop()
        if oz > z:
            tm[x][y].append((os, od, oz))
        else:
            tm[x][y].append((s, d, z))
    else:
        tm[x][y].append((s, d, z))


ans = 0
for c in range(C):
    for r in range(R):
        if m[r][c]:
            s, d, z = m[r][c].pop()
            ans += z
            break
    # 상어의 이동
    tm = [[[] for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if not m[x][y]:
                continue
            move(x, y)
    m = tm
print(ans)
