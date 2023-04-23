import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]


def bfs(x, y):
    m[x][y] = 2
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 0:
                m[nx][ny] = 2
                q.append((nx, ny))


t = 0
bfs(0, 0)
while True:
    removed = []
    for x in range(N):
        for y in range(M):
            if m[x][y] == 1:
                cnt = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 2:
                        cnt += 1
                if cnt >= 2:
                    removed.append((x, y))
    if not removed:
        break
    t += 1
    for x, y in removed:
        bfs(x, y)

print(t)
