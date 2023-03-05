import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, K = map(int, input().split())
m = list(map(int, input().split()))


def manipulate_and_serialize(m):
    tm = [row[:] for row in m]
    for x in range(len(m)):
        for y in range(len(m[0])):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(m) and 0 <= ny < len(m[0]) and m[x][y] > m[nx][ny] > 0:
                    d = (m[x][y] - m[nx][ny]) // 5
                    if d > 0:
                        tm[x][y] -= d
                        tm[nx][ny] += d
    m = []
    for y in range(len(tm[0])):
        for x in range(len(tm)):
            if tm[x][y] > 0:
                m.append(tm[x][y])
    return m


def simulate():
    global m
    min_cnt = min(m)
    for i in range(len(m)):
        if m[i] == min_cnt:
            m[i] += 1

    m = [m[1:], m[:1]]
    while len(m[0]) - len(m[1]) >= len(m):
        block = []
        for i in range(len(m)):
            block.append(m[i][:len(m[1])])
        tblock = [[0] * len(block) for _ in range(len(block[0]))]
        for x in range(len(block[1])):
            for y in range(len(block)):
                tblock[x][y] = block[y][len(block[0]) - 1 - x]
        m = [m[0][len(m[1]):]]
        m.extend(tblock)

    for x in range(1, len(m)):
        m[x].extend([0] * (len(m[0]) - len(m[x])))

    m = [manipulate_and_serialize(m)]

    for i in range(2):
        mid = len(m[0]) // 2
        block = []
        for r in range(len(m)):
            block.append(m[r][:mid])
        tblock = [[0] * len(block[0]) for _ in range(len(block))]
        for x in range(len(block)):
            for y in range(len(block[0])):
                tblock[x][y] = block[len(block) - 1 - x][len(block[0]) - 1 - y]
        tm = []
        for j in range(i + 1):
            tm.append(m[j][mid:])
        tm.extend(tblock)
        m = tm

    m = manipulate_and_serialize(tm)


ans = 0
while True:
    if max(m) - min(m) <= K:
        break
    simulate()
    ans += 1
print(ans)
