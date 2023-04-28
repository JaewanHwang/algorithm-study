import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
d = dict()
N, K = map(int, input().split())
m = list(map(int, input().split()))
q = deque(m)
cnt = 0
for x in m:
    d[x] = 0
while q and cnt < K:
    x = q.popleft()
    for i in (1, -1):
        nx = x + i
        if nx not in d:
            d[nx] = d[x] + 1
            q.append(nx)
            cnt += 1
            if cnt == K:
                break
ans = sum(d.values())
print(ans)
