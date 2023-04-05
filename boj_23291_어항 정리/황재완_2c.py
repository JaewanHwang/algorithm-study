import sys

sys.stdin = open('input.txt')
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, K = map(int, input().split())
m = [list(map(int, input().split()))]


def manipulate():
    global m
    R, C = len(m), len(m[0])
    tm = [[0] * C for _ in range(R)]
    for y in range(C):
        for x in range(R - 1, -1, -1):
            if m[x][y] == -1:
                continue
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < R and 0 <= ny < C and m[nx][ny] != -1:
                    diff = m[x][y] - m[nx][ny]
                    d = diff // 5
                    if diff > 0 and d > 0:
                        tm[x][y] -= d
                        tm[nx][ny] += d

    nm = [[]]
    for y in range(C):
        for x in range(R):
            if m[x][y] == -1:
                continue
            nm[0].append(m[x][y] + tm[x][y])
    m = nm


ans = 0
while True:
    min_val, max_val = min(m[0]), max(m[0])
    if max_val - min_val <= K:
        break
    for y in range(len(m[0])):
        if m[0][y] == min_val:
            m[0][y] += 1

    m.append([m[0][0]])
    m[0] = m[0][1:]
    while True:
        R, C = len(m), len(m[-1])
        if R > len(m[0]) - C:
            break
        b = []
        for x in range(R):
            b.append(m[x][:C])

        m = [m[0][C:]]
        R, C = C, R
        nb = [[0] * C for _ in range(R)]
        for x in range(R):
            for y in range(C):
                nb[x][y] = b[y][R - 1 - x]
        m.extend(nb)

    for x in range(1, len(m)):
        m[x].extend([-1] * (len(m[0]) - len(m[x])))

    manipulate()

    for _ in range(2):
        R, C = len(m), len(m[0]) // 2
        b = []
        for x in range(R):
            b.append(m[x][:C])
        tb = [[0] * C for _ in range(R)]
        for x in range(R):
            m[x] = m[x][C:]
            for y in range(C):
                tb[x][y] = b[R - 1 - x][C - 1 - y]
        m.extend(tb)
    manipulate()
    ans += 1
print(ans)
