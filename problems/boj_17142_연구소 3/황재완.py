import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
virus_list = []
BLANK_TOTAL_CNT = 0
for x in range(N):
    for y in range(N):
        if m[x][y] == 2:
            virus_list.append((x, y))
        elif m[x][y] == 0:
            BLANK_TOTAL_CNT += 1


def go(active_virus_list):
    d = [[-1] * N for _ in range(N)]
    q = deque(active_virus_list)
    diffuse_cnt = 0
    max_dist = 0
    for x, y in active_virus_list:
        d[x][y] = 0
    while q:
        x, y = q.popleft()
        if m[x][y] == 0:
            max_dist = max(max_dist, d[x][y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and d[nx][ny] == -1 and m[nx][ny] != 1:
                if m[nx][ny] == 0:
                    diffuse_cnt += 1
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
    if BLANK_TOTAL_CNT == diffuse_cnt:
        return max_dist
    return -1



ans = -1
for case in combinations(virus_list, r=M):
    res = go(case)
    ans = res if ans == -1 else res if 0 <= res < ans else ans
print(ans)
