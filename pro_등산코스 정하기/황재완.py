from collections import deque


def ok(k, adj_list, gates, summits, ans):
    q = deque(gates)
    visited = [False] * len(adj_list)
    min_summit = 0
    for gate in gates:
        visited[gate] = True
    while q:
        x = q.popleft()
        if x in summits:
            if min_summit == 0 or (min_summit > x):
                min_summit = x
            continue
        for w, y in adj_list[x]:
            if w > k:
                break
            if not visited[y]:
                visited[y] = True
                q.append(y)

    if not min_summit:
        return False
    ans[0], ans[1] = min_summit, k
    return True


def solution(n, paths, gates, summits):
    ans = [0, 0]
    adj_list = [[] for _ in range(n + 1)]
    max_w = 1
    summits = set(summits)
    for x, y, w in paths:
        max_w = max(max_w, w)
        adj_list[x].append((w, y))
        adj_list[y].append((w, x))
    for x in range(1, n + 1):
        adj_list[x].sort()

    l, r = 1, max_w
    while l <= r:
        mid = (l + r) // 2
        if ok(mid, adj_list, gates, summits, ans):
            r = mid - 1
        else:
            l = mid + 1

    return ans
