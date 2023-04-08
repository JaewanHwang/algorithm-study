import sys
from collections import deque
import math

sys.stdin = open('input.txt')

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
dir_map = {1: ((1,), (0, 1), (2, 1)),
           2: ((3,), (2, 3), (0, 3)),
           3: ((0,), (3, 0), (1, 0)),
           4: ((2,), (1, 2), (3, 2))}
R, C, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R)]
heaters = []
check_cells = []
for x in range(R):
    for y in range(C):
        if 1 <= m[x][y] <= 4:
            heaters.append((x, y, m[x][y]))
            m[x][y] = 0
        elif m[x][y] == 5:
            check_cells.append((x, y))
            m[x][y] = 0
W = int(input())
w = [[[[False] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
for _ in range(W):
    x, y, t = map(int, input().split())
    x, y = x - 1, y - 1
    if t == 0:
        w[x][y][x - 1][y] = w[x - 1][y][x][y] = True
    else:
        w[x][y][x][y + 1] = w[x][y + 1][x][y] = True


def turn_heater_on(hx, hy, hd):
    dist = [[-1] * C for _ in range(R)]
    sx, sy = hx + dx[dir_map[hd][0][0]], hy + dy[dir_map[hd][0][0]]
    q = deque([(sx, sy)])
    dist[sx][sy] = 5
    while q:
        cur_x, cur_y = q.popleft()
        m[cur_x][cur_y] += dist[cur_x][cur_y]
        if dist[cur_x][cur_y] == 1:
            continue
        for dirs in dir_map[hd]:
            x, y = cur_x, cur_y
            failed = False
            for k in dirs:
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= R or ny < 0 or ny >= C or w[x][y][nx][ny]:
                    failed = True
                    break
                x, y = nx, ny
            if not failed and dist[x][y] == -1:
                q.append((x, y))
                dist[x][y] = dist[cur_x][cur_y] - 1


def simulate():
    global m

    # 온풍기에서 바람 나옴
    for x, y, d in heaters:
        turn_heater_on(x, y, d)

    # 온도가 조절됨
    tm = [row[:] for row in m]
    for x in range(R):
        for y in range(C):
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < R and 0 <= ny < C and not w[x][y][nx][ny] and m[x][y] > m[nx][ny]:
                    move_amount = math.floor((m[x][y] - m[nx][ny]) / 4)
                    tm[x][y] -= move_amount
                    tm[nx][ny] += move_amount
    m = tm

    # 바깥쪽 온도 1씩 감소
    for y in range(C):
        for x in (0, R - 1):
            if m[x][y] >= 1:
                m[x][y] -= 1
    for x in range(1, R - 1):
        for y in (0, C - 1):
            if m[x][y] >= 1:
                m[x][y] -= 1

    # 조사하는 칸이 모두 K이상 되었는지 검사
    for x, y in check_cells:
        if m[x][y] < K:
            return False
    return True


for ans in range(1, 102):
    if simulate():
        break
print(ans)
