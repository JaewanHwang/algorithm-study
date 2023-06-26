import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
A, B, N, M = map(int, input().split())
delta = (-1, 1, -A, A, -B, B)
q = deque([N])
d = [-1] * 100_001
d[N] = 0
while q:
    x = q.popleft()
    for k in delta:
        nx = x + k
        if 0 <= nx <= 100_000 and d[nx] == -1:
            d[nx] = d[x] + 1
            q.append(nx)
    for k in (A, B):
        nx = x * k
        if 0 <= nx <= 100_000 and d[nx] == -1:
            d[nx] = d[x] + 1
            q.append(nx)
print(d[M])
