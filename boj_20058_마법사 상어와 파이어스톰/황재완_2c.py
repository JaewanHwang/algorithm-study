import sys
from collections import deque

sys.stdin = open('input.txt')
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, Q = map(int, input().split())
LEN = 2 ** N
m = [list(map(int, input().split())) for _ in range(LEN)]


def simulate(l):
    global m
    SIZE = 2 ** l
    tm = [[0] * LEN for _ in range(LEN)]
    for sx in range(0, LEN, SIZE):
        for sy in range(0, LEN, SIZE):
            for x in range(sx, sx + SIZE):
                for y in range(sy, sy + SIZE):
                    tm[x][y] = m[sx + SIZE - 1 - y + sy][sy + x - sx]
    m = tm
    tm = [[0] * LEN for _ in range(LEN)]
    for x in range(LEN):
        for y in range(LEN):
            if m[x][y] == 0:
                continue
            cnt = 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < LEN and 0 <= ny < LEN and m[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                tm[x][y] -= 1
    for x in range(LEN):
        for y in range(LEN):
            m[x][y] += tm[x][y]


for l in map(int, input().split()):
    simulate(l)

ans = 0
tot = 0


def bfs(x, y):
    global ans, tot
    tot += m[x][y]
    size = 1
    q = deque([(x, y)])
    m[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < LEN and 0 <= ny < LEN and m[nx][ny] > 0:
                tot += m[nx][ny]
                size += 1
                m[nx][ny] = 0
                q.append((nx, ny))
    ans = max(ans, size)


ans, tot = 0, 0
for x in range(LEN):
    for y in range(LEN):
        if m[x][y] > 0:
            bfs(x, y)
print(tot, ans, sep='\n')
