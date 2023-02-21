import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, -1, -1, -1, 0, 1, 1, 1)
fish_dict = dict()
m = [[0] * 4 for _ in range(4)]
for x in range(4):
    line = list(map(int, input().split()))
    for y in range(0, 4):
        a, b = line[2 * y], line[2 * y + 1]
        m[x][y] = a
        fish_dict[a] = [x, y, b - 1]
ans = 0


def go(sx, sy, tot, m, fish_dict):
    global ans
    tot += m[sx][sy]
    ans = max(ans, tot)
    sx, sy, sd = fish_dict.pop(m[sx][sy])
    m[sx][sy] = 0
    for num in sorted(fish_dict):
        x, y, d = fish_dict[num]
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
            fish_dict[num] = [nx, ny, d]
            if m[nx][ny] > 0:
                fish_dict[m[nx][ny]][0], fish_dict[m[nx][ny]][1] = x, y
            m[nx][ny], m[x][y] = m[x][y], m[nx][ny]
        else:
            for _ in range(8):
                d = (d + 1) % 8
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                    fish_dict[num] = [nx, ny, d]
                    if m[nx][ny] > 0:
                        fish_dict[m[nx][ny]][0], fish_dict[m[nx][ny]][1] = x, y
                    m[nx][ny], m[x][y] = m[x][y], m[nx][ny]
                    break

    while 0 <= sx + dx[sd] < 4 and 0 <= sy + dy[sd] < 4:
        sx += dx[sd]
        sy += dy[sd]
        if m[sx][sy] > 0:
            go(sx, sy, tot, [row[:] for row in m], {key: val[:] for key, val in fish_dict.items()})


go(0, 0, 0, m, fish_dict)
print(ans)
