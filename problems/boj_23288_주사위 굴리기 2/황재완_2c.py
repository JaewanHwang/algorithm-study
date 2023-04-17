import sys
from collections import deque

sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
group = [[-1] * M for _ in range(N)]
dice = list(range(7))
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
score = []


def bfs(sx, sy):
    q = deque([(sx, sy)])
    group[sx][sy] = len(score)
    size = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == m[sx][sy] and group[nx][ny] == -1:
                q.append((nx, ny))
                group[nx][ny] = len(score)
                size += 1
    score.append(size)


for x in range(N):
    for y in range(M):
        if group[x][y] == -1:
            bfs(x, y)


def simulate():
    global ans, x, y, d

    nx, ny, nd = x + dx[d], y + dy[d], d
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nd = (d + 2) % 4
        nx, ny = x + dx[nd], y + dy[nd]

    if nd == 0:
        dice[4], dice[1], dice[3], dice[6] = dice[6], dice[4], dice[1], dice[3]
    elif nd == 1:
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]
    elif nd == 2:
        dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
    else:
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]

    ans += score[group[nx][ny]] * m[nx][ny]

    A, B = dice[6], m[nx][ny]
    if A > B:
        nd = (nd + 1) % 4
    elif A < B:
        nd = (nd - 1) % 4

    x, y, d = nx, ny, nd


ans = 0
x, y, d = 0, 0, 0
for _ in range(K):
    simulate()
print(ans)
