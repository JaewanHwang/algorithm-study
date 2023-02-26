import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, Q = map(int, input().split())
NN = 2 ** N
m = [list(map(int, input().split())) for _ in range(NN)]


def simulate(m, L):
    LL = 2 ** L
    tm = [[0] * NN for _ in range(NN)]
    for sx in range(0, NN, LL):
        for sy in range(0, NN, LL):
            for x in range(LL):
                for y in range(LL):
                    tm[sx + x][sy + y] = m[sx + LL - 1 - y][sy + x]

    decrease_list = []
    for x in range(NN):
        for y in range(NN):
            if tm[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < NN and 0 <= ny < NN and tm[nx][ny] != 0:
                        cnt += 1
                if cnt < 3:
                    decrease_list.append((x, y))
    for x, y in decrease_list:
        tm[x][y] -= 1
    return tm


def bfs(x, y):
    q = deque([(x, y)])
    m[x][y] = 0
    tot = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < NN and 0 <= ny < NN and m[nx][ny] != 0:
                tot += 1
                m[nx][ny] = 0
                q.append((nx, ny))
    return tot


for L in map(int, input().split()):
    m = simulate(m, L)

print(sum(sum(row) for row in m))
ans = 0
for x in range(NN):
    for y in range(NN):
        if m[x][y] != 0:
            ans = max(ans, bfs(x, y))
print(ans)
