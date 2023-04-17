# 풀이1: 효율성 테스트 통과못함
from itertools import combinations
from collections import deque


def bfs(n, num, adj_list, cutting_edges, visited):
    cnt = num[n]
    visited[n] = True
    q = deque([n])
    while q:
        x = q.popleft()
        for y in adj_list[x]:
            if (x, y) in cutting_edges or (y, x) in cutting_edges:
                continue
            if not visited[y]:
                visited[y] = True
                q.append(y)
                cnt += num[y]
    return cnt


def solution(k, num, links):
    adj_list = [[] for _ in range(len(num))]
    edges = []
    for i, (l, r) in enumerate(links):
        if l != -1:
            edges.append((i, l))
            adj_list[i].append(l)
            adj_list[l].append(i)
        if r != -1:
            edges.append((i, r))
            adj_list[i].append(r)
            adj_list[r].append(i)
    ans = 1e9
    for case in combinations(edges, r=k - 1):
        cutting_edges = set(case)
        visited = [False] * len(num)
        max_cnt = 0
        for i in range(len(num)):
            if not visited[i]:
                max_cnt = max(bfs(i, num, adj_list, cutting_edges, visited), max_cnt)
        ans = min(ans, max_cnt)
    return ans
