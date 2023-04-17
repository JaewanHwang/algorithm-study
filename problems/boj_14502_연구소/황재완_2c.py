import sys
from collections import deque
from itertools import combinations

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]


def simulate(case):
    diffuse_cnt = 0
    board = [row[:] for row in m]
    for x, y in case:
        board[x][y] = 1
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                diffuse_cnt += 1
    return len(candidates) - 3 - diffuse_cnt


candidates = []
viruses = []
for x in range(N):
    for y in range(M):
        if m[x][y] == 0:
            candidates.append((x, y))
        elif m[x][y] == 2:
            viruses.append((x, y))

ans = 0
for case in combinations(candidates, r=3):
    ans = max(ans, simulate(case))
print(ans)
