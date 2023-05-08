import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y, w = map(int, input().split())
    tree[x].append((y, w))
    tree[y].append((x, w))
for _ in range(M):
    s, e = map(int, input().split())
    q = deque([s])
    d = [-1] * (N + 1)
    d[s] = 0
    while q:
        cur = q.popleft()
        if cur == e:
            break
        for nxt, w in tree[cur]:
            if d[nxt] == -1:
                d[nxt] = d[cur] + w
                q.append(nxt)

    print(d[e])
