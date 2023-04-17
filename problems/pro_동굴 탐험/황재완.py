import sys

sys.setrecursionlimit(10 ** 6)


def go(x, visited, ordered_set, unordered_set, cnt):
    if cnt == N:
        return True

    for y in adj_list[x]:
        if not visited[y]:
            if y in post and not visited[post[y]]:
                ordered_set.add(y)
            else:
                unordered_set.add(y)

    if not unordered_set:
        return False

    y = unordered_set.pop()
    visited[y] = True
    if y in prev and prev[y] in ordered_set:
        ordered_set.remove(prev[y])
        unordered_set.add(prev[y])

    return go(y, visited, ordered_set, unordered_set, cnt + 1)


adj_list, post, prev, N = None, None, None, None


def solution(n, path, order):
    global adj_list, post, prev, N
    N = n
    post = dict()
    prev = dict()
    for x, y in order:
        post[y] = x
        prev[x] = y
    adj_list = [[] for _ in range(n)]
    for x, y in path:
        adj_list[x].append(y)
        adj_list[y].append(x)
    visited = [False] * n
    if 0 in post and not visited[post[0]]:
        return False
    visited[0] = True
    return go(0, visited, set(), set(), 1)
