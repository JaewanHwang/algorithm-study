import sys

sys.setrecursionlimit(10 ** 6)

order_map = dict()
reverse_order_map = dict()
adj_list = None
visited = None
ok = None
ready = set()
N = 0


def go(cur, cnt, candidates):
    visited[cur] = True
    cnt += 1
    if cur in reverse_order_map:
        ok[reverse_order_map[cur]] = True
        if reverse_order_map[cur] in ready:
            ready.remove(reverse_order_map[cur])
            candidates.append(reverse_order_map[cur])

    if cnt == N:
        return True

    for v in adj_list[cur]:
        if visited[v]:
            continue
        if v not in order_map or ok[v]:
            candidates.append(v)
        else:
            ready.add(v)

    if not candidates:
        return False

    next = candidates.pop()
    return go(next, cnt, candidates)


def solution(n, path, order):
    global adj_list, visited, N, ok
    N = n
    adj_list = [set() for _ in range(n)]
    visited = [False] * N
    ok = [False] * N
    for u, v in order:
        if v == 0:
            return False
        order_map[v] = u
        reverse_order_map[u] = v
    for u, v in path:
        adj_list[u].add(v)
        adj_list[v].add(u)
    return go(0, 0, [])
