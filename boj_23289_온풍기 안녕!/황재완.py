import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

hdx, hdy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
R, C, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R)]
heater_dir_map = [{2: (2,), 1: (0, 2), 3: (4, 2)},  # λ
                  {6: (6,), 5: (4, 6), 7: (0, 6)},  # μ
                  {0: (0,), 7: (6, 0), 1: (2, 0)},  # λΆ
                  {4: (4,), 3: (2, 4), 5: (6, 4)}]  # λ¨

heater_l = []
investigate_l = []
for x in range(R):
    for y in range(C):
        if 1 <= m[x][y] <= 4:
            heater_l.append((x, y, m[x][y] - 1))
            m[x][y] = 0
        elif m[x][y] == 5:
            investigate_l.append((x, y))
            m[x][y] = 0
w = [[[[False] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
W = int(input())
for _ in range(W):
    x, y, t = map(int, input().split())
    x, y = x - 1, y - 1
    if t == 0:
        w[x][y][x - 1][y] = w[x - 1][y][x][y] = True
    else:
        w[x][y][x][y + 1] = w[x][y + 1][x][y] = True


def turn_heater_on():
    for x, y, d in heater_l:
        visited = [[False] * C for _ in range(R)]
        q = deque([(x + dx[d], y + dy[d], 5)])
        while q:
            x, y, k = q.popleft()
            m[x][y] += k
            if k == 1:
                continue
            for key, val in heater_dir_map[d].items():
                nx, ny = x, y
                failed = False
                for v in val:
                    if 0 <= nx + hdx[v] < R and 0 <= ny + hdy[v] < C and not w[nx][ny][nx + hdx[v]][ny + hdy[v]]:
                        nx, ny = nx + hdx[v], ny + hdy[v]
                    else:
                        failed = True
                        break
                if failed:
                    continue
                if not visited[nx][ny]:
                    q.append((nx, ny, k - 1))
                    visited[nx][ny] = True


def manipulate_temperature():
    global m
    tm = [row[:] for row in m]
    for x in range(R):
        for y in range(C):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and m[x][y] > m[nx][ny] and not w[x][y][nx][ny]:
                    diff = (m[x][y] - m[nx][ny]) // 4
                    tm[x][y] -= diff
                    tm[nx][ny] += diff
    m = tm


def decrease_side_temperature():
    for x in (0, R - 1):
        for y in range(C):
            if m[x][y] > 0:
                m[x][y] -= 1
    for y in (0, C - 1):
        for x in range(1, R - 1):
            if m[x][y] > 0:
                m[x][y] -= 1


def investigate_temperature():
    for x, y in investigate_l:
        if m[x][y] < K:
            return False
    return True


def simulate():
    # 1. μ§μ μλ λͺ¨λ  μ¨νκΈ°μμ λ°λμ΄ ν λ² λμ΄
    turn_heater_on()
    # 2. μ¨λκ° μ‘°μ λ¨
    manipulate_temperature()
    # 3. μ¨λκ° 1 μ΄μμΈ κ°μ₯ λ°κΉ₯μͺ½ μΉΈμ μ¨λκ° 1μ© κ°μ
    decrease_side_temperature()
    # 4. μ΄μ½λ¦Ώμ νλ λ¨Ήλλ€.
    ...
    # 5. μ‘°μ¬νλ λͺ¨λ  μΉΈμ μ¨λκ° K μ΄μμ΄ λμλμ§ κ²μ¬. λͺ¨λ  μΉΈμ μ¨λκ° Kμ΄μμ΄λ©΄ νμ€νΈλ₯Ό μ€λ¨νκ³ , μλλ©΄ 1λΆν° λ€μ μμνλ€.
    return investigate_temperature()


for ans in range(1, 102):
    if simulate():
        break

print(ans)
