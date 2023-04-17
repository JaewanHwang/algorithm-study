from collections import deque


def go(mid, adj_list, gates, summits):
    visited = [False] * (N + 1)
    min_summit = N + 1
    for start in gates:
        q = deque([start])
        visited[start] = True
        while q:
            u = q.popleft()
            if u in summits:
                min_summit = min(min_summit, u)
                continue
            for (w, v) in adj_list[u]:
                if v in gates or w > mid or visited[v]:
                    continue
                q.append(v)
                visited[v] = True
    return min_summit


N = 0


def solution(n, paths, gates, summits):
    global N
    N = n
    adj_list = [[] for _ in range(N + 1)]
    max_w = 0
    for u, v, w in paths:
        adj_list[u].append((w, v))
        adj_list[v].append((w, u))
        max_w = max(max_w, w)
    gates, summits = set(gates), set(summits)

    l, r = 1, max_w
    while l <= r:
        mid = (l + r) // 2
        res = go(mid, adj_list, gates, summits)
        if res != N + 1:
            ans = [res, mid]
            r = mid - 1
        else:
            l = mid + 1
    return ans


print(
    solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
