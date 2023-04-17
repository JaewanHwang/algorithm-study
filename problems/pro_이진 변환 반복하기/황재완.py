from collections import deque


def solution(n, edges):
    tree = [[] for _ in range(n + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    d = [-1] * (n + 1)
    q = deque([1])
    d[1] = 0
    while q:
        cur = q.popleft()
        for v in tree[cur]:
            if d[v] == -1:
                d[v] = d[cur] + 1
                q.append(v)
    start = d.index(max(d))
    q = deque([start])
    print(q)
    d = [-1] * (n + 1)
    d[start] = 0
    while q:
        cur = q.popleft()
        for v in tree[cur]:
            if d[v] == -1:
                d[v] = d[cur] + 1
                q.append(v)
    start = d.index(max(d))
    d.sort(reverse=True)
    if d[0] != d[1]:
        q = deque([start])
        d = [-1] * (n + 1)
        d[start] = 0
        while q:
            cur = q.popleft()
            for v in tree[cur]:
                if d[v] == -1:
                    d[v] = d[cur] + 1
                    q.append(v)
        d.sort(reverse=True)
        if d[0] != d[1]:
            return d[0] - 1
        else:
            return d[0]
    else:
        return d[0]


print(solution(4, [[1, 2], [2, 3], [3, 4]]))
