import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    pi, qi, ri = map(int, input().split())
    graph[pi].append((qi, ri))
    graph[qi].append((pi, ri))


def bfs(start):
    q = deque([start])
    d[start][start] = float('inf')
    while q:
        cur = q.popleft()
        for nxt, cost in graph[cur]:
            if d[start][nxt] == -1:
                d[start][nxt] = min(d[start][cur], cost)
                q.append(nxt)


d = [[-1] * (N + 1) for _ in range(N + 1)]
for node in range(1, N + 1):
    bfs(node)

for _ in range(Q):
    ki, vi = map(int, input().split())
    ans = 0
    for ui in range(1, N + 1):
        if ui == vi:
            continue
        if d[vi][ui] >= ki:
            ans += 1
    print(ans)
