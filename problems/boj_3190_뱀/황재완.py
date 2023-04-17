import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
N, K = int(input()), int(input())
ma = [[False] * N for _ in range(N)]
ms = [[False] * N for _ in range(N)]
ms[0][0] = True
s = deque([(0, 0, 1)])
for _ in range(K):
    x, y = map(lambda x: int(x) - 1, input().split())
    ma[x][y] = True
L = int(input())
op = deque()
for _ in range(L):
    t, o = input().split()
    op.append((int(t), -1 if o == 'L' else 1))


sec = 0
while True:
    sx, sy, sd = s[-1]
    if op and op[0][0] == sec:
        t, o = op.popleft()
        sd = (sd + o) % 4

    sx, sy = sx + dx[sd], sy + dy[sd]
    sec += 1
    if sx < 0 or sx >= N or sy < 0 or sy >= N or ms[sx][sy]:
        break
    if ma[sx][sy]:
        ma[sx][sy] = False
        ms[sx][sy] = True
        s.append((sx, sy, sd))
    else:
        tsx, tsy, _ = s.popleft()
        ms[tsx][tsy] = False
        s.append((sx, sy, sd))
        ms[sx][sy] = True
ans = sec
print(ans)


