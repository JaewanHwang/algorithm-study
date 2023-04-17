import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (1, 0), (0, 1)
N, L, R = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def bfs(x, y):
    q = deque([(x, y)])
    group_tot.append(m[x][y])
    group_cnt.append(1)
    gm[x][y] = len(group_tot) - 1
    while q:
        x, y = q.popleft()
        for nx, ny in adj_list[x][y]:
            if gm[nx][ny] == -1:
                gm[nx][ny] = len(group_tot) - 1
                group_tot[-1] += m[nx][ny]
                group_cnt[-1] += 1
                q.append((nx, ny))
    group_tot[-1] = group_tot[-1] // group_cnt[-1]


while True:
    group_tot = []
    group_cnt = []
    gm = [[-1] * N for _ in range(N)]
    moved = False
    adj_list = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for k in range(2):
                if (x == N - 1 and k == 0) or (y == N - 1 and k == 1):
                    continue
                nx, ny = x + dx[k], y + dy[k]
                if L <= abs(m[x][y] - m[nx][ny]) <= R:
                    moved = True
                    adj_list[x][y].append((nx, ny))
                    adj_list[nx][ny].append((x, y))
    if not moved:
        break

    for x in range(N):
        for y in range(N):
            if gm[x][y] == -1:
                bfs(x, y)

    for x in range(N):
        for y in range(N):
            m[x][y] = group_tot[gm[x][y]]
    ans += 1
print(ans)
