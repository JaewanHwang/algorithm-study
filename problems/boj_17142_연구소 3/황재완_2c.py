import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
viruses = []
BLANK_CNT = 0
for x in range(N):
    for y in range(N):
        if m[x][y] == 2:
            viruses.append((x, y))
        elif m[x][y] == 0:
            BLANK_CNT += 1


def simulate(case):
    d = [[-1] * N for _ in range(N)]
    for x, y in case:
        d[x][y] = 0
    q = deque(case)

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and m[nx][ny] != 1 and d[nx][ny] == -1:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1

    res = 0
    for x in range(N):
        for y in range(N):
            if m[x][y] == 0:
                if d[x][y] == -1:
                    return -1
                res = max(res, d[x][y])
    return res


ans = -1
for case in combinations(viruses, r=M):
    res = simulate(case)
    if ans == -1 or ans > res >= 0:
        ans = res
print(ans)
