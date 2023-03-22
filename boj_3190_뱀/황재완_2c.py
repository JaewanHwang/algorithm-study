import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
N = int(input())
m = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(lambda x: int(x) - 1, input().split())
    m[x][y] = 2
L = int(input())
change_dir = [0] * 10_001
for _ in range(L):
    ct, op = input().split()
    change_dir[int(ct)] = 1 if op == 'D' else -1

t = 0
d = 1
m[0][0] = 1
snake = deque([(0, 0)])
while True:
    nd = (d + change_dir[t]) % 4
    x, y = snake[-1]
    nx, ny = x + dx[nd], y + dy[nd]
    t += 1
    if nx < 0 or nx >= N or ny < 0 or ny >= N or m[nx][ny] == 1:
        break
    snake.append((nx, ny))
    if m[nx][ny] == 0:
        tx, ty = snake.popleft()
        m[tx][ty] = 0
    m[nx][ny] = 1
    d = nd

ans = t
print(ans)
