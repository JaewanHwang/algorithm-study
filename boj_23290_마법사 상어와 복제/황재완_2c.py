import sys
from collections import defaultdict

sys.stdin = open('input.txt')

M, S = map(int, input().split())
fdx, fdy = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)
sdx, sdy = (0, -1, 0, 1, 0), (0, 0, -1, 0, 1)
m = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
for _ in range(M):
    x, y, d = map(lambda x: int(x) - 1, input().split())
    m[x][y][d] += 1
sx, sy = map(lambda x: int(x) - 1, input().split())
smell = [[0] * 4 for _ in range(4)]


def move(x, y, tm):
    for d in list(m[x][y]):
        for k in range(8):
            nd = (d - k) % 8
            nx, ny = x + fdx[nd], y + fdy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 and (sx, sy) != (nx, ny) and smell[nx][ny] == 0:
                tm[nx][ny][nd] += m[x][y].pop(d)
                break
        else:
            tm[x][y][d] += m[x][y].pop(d)


def go(n, x, y, tot, candidates, case, visited):
    if n == 3:
        candidates.append((tot, list(map(str, case[:]))))
        return
    for k in range(1, 5):
        nx, ny = x + sdx[k], y + sdy[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            case[n] = k
            visited[nx][ny] += 1
            go(n + 1, nx, ny, tot + (sum(m[nx][ny].values()) if visited[nx][ny] == 1 else 0), candidates, case, visited)
            visited[nx][ny] -= 1


def simulate():
    global m, sx, sy
    copy = [[defaultdict(int, cell) for cell in row] for row in m]
    tm = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if m[x][y]:
                move(x, y, tm)
    m = tm
    candidates = []
    visited = [[0] * 4 for _ in range(4)]
    case = [0, 0, 0]
    go(0, sx, sy, 0, candidates, case, visited)
    _, best_case = max(candidates, key=lambda x: (x[0], -int(''.join(x[1]))))
    for k in best_case:
        k = int(k)
        nsx, nsy = sx + sdx[k], sy + sdy[k]
        if m[nsx][nsy]:
            m[nsx][nsy] = defaultdict(int)
            smell[nsx][nsy] = 3
        sx, sy = nsx, nsy

    for x in range(4):
        for y in range(4):
            if smell[x][y] == 0:
                continue
            smell[x][y] -= 1

    for x in range(4):
        for y in range(4):
            if copy[x][y]:
                for key, val in copy[x][y].items():
                    m[x][y][key] += val


for _ in range(S):
    simulate()
ans = 0
for x in range(4):
    for y in range(4):
        ans += sum(m[x][y].values())
print(ans)
