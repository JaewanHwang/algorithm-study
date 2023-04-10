import sys
from itertools import product
from collections import deque

sys.stdin = open("input.txt", "r")

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(sx, sy, m):
    q = deque([(sx, sy, m[sx][sy])])
    res = 1
    m[sx][sy] = 0
    while q:
        cur_x, cur_y, l = q.popleft()
        for k in range(4):
            x, y = cur_x, cur_y
            for _ in range(l - 1):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < H and 0 <= ny < W:
                    if m[nx][ny] > 0:
                        q.append((nx, ny, m[nx][ny]))
                        res += 1
                        m[nx][ny] = 0
                else:
                    break
                x, y = nx, ny

    for y in range(W):
        last_x = H - 1
        for x in range(H - 1, -1, -1):
            if m[x][y] > 0:
                m[x][y], m[last_x][y] = 0, m[x][y]
                last_x -= 1

    return res


def simulate(case):
    global ans
    res = 0
    m = [row[:] for row in original_m]
    for y in case:
        for x in range(H):
            if m[x][y] > 0:
                res += go(x, y, m)
                break
    ans = min(ans, TOTAL_BLOCK - res)


T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    original_m = [list(map(int, input().split())) for _ in range(H)]
    TOTAL_BLOCK = 0
    for x in range(H):
        for y in range(W):
            if original_m[x][y] > 0:
                TOTAL_BLOCK += 1
    ans = W * H
    for case in product(range(W), repeat=N):
        simulate(case)
        if ans == 0:
            break
    print(f'#{test_case} {ans}')
