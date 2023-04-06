import sys
from collections import deque

sys.stdin = open("input.txt", "r")


def go(i, tot, m):
    global ans
    if i == N:
        ans = min(ans, tot)
        return
    for y in range(W):
        for x in range(H):
            if m[x][y] > 0:
                break
        tm = [row[:] for row in m]
        if m[x][y] > 0:
            removed = bomb(x, y, tm)
        else:
            removed = 0
        go(i + 1, tot - removed, tm)


def move(m):
    for y in range(W):
        last_x = H - 1
        for x in range(H - 1, -1, -1):
            if m[x][y] == 0:
                continue
            m[x][y], m[last_x][y] = 0, m[x][y]
            last_x -= 1


def bomb(x, y, m):
    res = 0
    q = deque([(x, y)])
    checked = [[False] * W for _ in range(H)]
    checked[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            for i in range(1, m[x][y]):
                nx, ny = x + dx[k] * i, y + dy[k] * i
                if 0 <= nx < H and 0 <= ny < W:
                    if m[nx][ny] > 0 and not checked[nx][ny]:
                        checked[nx][ny] = True
                        q.append((nx, ny))
                else:
                    break
    for x in range(H):
        for y in range(W):
            if checked[x][y]:
                res += 1
                m[x][y] = 0
    move(m)

    return res


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(H)]
    tot = 0
    for x in range(H):
        for y in range(W):
            if m[x][y] > 0:
                tot += 1
    ans = tot
    go(0, tot, m)
    print(f'#{test_case} {ans}')
