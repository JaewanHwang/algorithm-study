import sys
from itertools import product
from collections import deque

sys.stdin = open("input.txt", "r")
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(y, m):
    q = deque()
    for x in range(H):
        if m[x][y] > 0:
            q.append((x, y, m[x][y]))
            m[x][y] = 0
            break
    while q:
        x, y, d = q.popleft()
        for k in range(4):
            nx, ny = x, y
            for _ in range(d - 1):
                nx, ny = nx + dx[k], ny + dy[k]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    break
                if m[nx][ny] > 0:
                    q.append((nx, ny, m[nx][ny]))
                    m[nx][ny] = 0

    for y in range(W):
        last_x = H - 1
        for x in range(H - 1, -1, -1):
            if m[x][y] > 0:
                tmp = m[x][y]
                m[x][y] = 0
                m[last_x][y] = tmp
                last_x -= 1


def simulate():
    min_remain_cnt = W * H
    for case in product(range(W), repeat=N):
        m = [row[:] for row in original_m]
        for y in case:
            go(y, m)
        remain_cnt = 0
        for x in range(H):
            for y in range(W):
                if m[x][y] > 0:
                    remain_cnt += 1
        min_remain_cnt = min(min_remain_cnt, remain_cnt)
        if min_remain_cnt == 0:
            break
    return min_remain_cnt


T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    original_m = [list(map(int, input().split())) for _ in range(H)]
    ans = simulate()
    print(f'#{test_case} {ans}')
