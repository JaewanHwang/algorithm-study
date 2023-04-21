import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(green, red):
    global ans
    d = [[-1] * M for _ in range(N)]
    q = deque()
    for x, y in green:
        d[x][y] = [0, 0]  # time, color
        q.append((x, y, 0))
    for x, y in red:
        d[x][y] = [0, 1]
        q.append((x, y, 1))
    res = 0
    while q:
        x, y, c, = q.popleft()
        if d[x][y][1] == 2:
            continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] != 0:
                if d[nx][ny] == -1:
                    q.append((nx, ny, c))
                    d[nx][ny] = [d[x][y][0] + 1, c]
                elif d[nx][ny][1] == 1 - d[x][y][1] and d[nx][ny][0] == d[x][y][0] + 1:
                    res += 1
                    d[nx][ny][1] = 2

    ans = max(ans, res)


N, M, G, R = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
candidates = []
for x in range(N):
    for y in range(M):
        if m[x][y] == 2:
            candidates.append((x, y))
ans = 0
for case in combinations(candidates, r=G + R):
    case = set(case)
    for green in combinations(case, r=G):
        go(green, case - set(green))
print(ans)
