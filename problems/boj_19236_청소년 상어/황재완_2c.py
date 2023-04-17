import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, -1, -1, -1, 0, 1, 1, 1)
fishes = {}
m = [[0] * 4 for _ in range(4)]
for x in range(4):
    row = list(map(int, input().split()))
    for y in range(0, 8, 2):
        ai, bi = row[y:y + 2]
        fishes[ai] = [x, y // 2, bi - 1]
        m[x][y // 2] = ai


def go(eaten_fish, tot, m, fishes):
    m = [row[:] for row in m]
    fishes = {key: val[:] for key, val in fishes.items()}

    sx, sy, sd = fishes.pop(eaten_fish)
    tot += m[sx][sy]
    m[sx][sy] = 0

    for f_num in sorted(fishes):
        x, y, d = fishes[f_num]
        for k in range(8):
            nd = (d + k) % 8
            fishes[f_num][2] = nd
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 and (sx, sy) != (nx, ny):
                if m[nx][ny]:
                    fishes[f_num][:2], fishes[m[nx][ny]][:2] = fishes[m[nx][ny]][:2], fishes[f_num][:2]
                else:
                    fishes[f_num][:2] = [nx, ny]
                m[nx][ny], m[x][y] = m[x][y], m[nx][ny]
                break

    res = tot
    while 0 <= sx < 4 and 0 <= sy < 4:
        nsx, nsy = sx + dx[sd], sy + dy[sd]
        if 0 <= nsx < 4 and 0 <= nsy < 4 and m[nsx][nsy]:
            res = max(res, go(m[nsx][nsy], tot, m, fishes))
        sx, sy = nsx, nsy

    return res


ans = go(m[0][0], 0, m, fishes)
print(ans)
