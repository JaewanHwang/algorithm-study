import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    graph = [[] for _ in range(m)]
    tot = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        tot += z
        graph[x].append((y, z))
        graph[y].append((x, z))

    visited = [False] * m
    min_edge = [float('inf')] * m
    min_edge[0] = 0
    pq = []
    heappush(pq, (0, 0))
    cnt = 0
    res = 0
    while pq:
        cost, cur = heappop(pq)
        if visited[cur]:
            continue
        visited[cur] = True
        res += cost
        cnt += 1
        if cnt == m:
            break
        for nxt, cost in graph[cur]:
            if not visited[nxt] and min_edge[nxt] > cost:
                min_edge[nxt] = cost
                heappush(pq, (cost, nxt))
    print(tot - res)
