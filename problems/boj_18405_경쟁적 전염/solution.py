import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus = []
for x in range(N):
    for y in range(N):
        if m[x][y] > 0:
            virus.append((m[x][y], x, y))
q = deque(sorted(virus))
for _ in range(S):
    for _ in range(len(q)):
        num, x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or m[nx][ny] != 0:
                continue
            m[nx][ny] = num
            q.append((num, nx, ny))
    if m[X - 1][Y - 1] != 0:
        break
print(m[X - 1][Y - 1])
