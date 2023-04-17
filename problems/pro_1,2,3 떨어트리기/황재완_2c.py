from collections import deque
from itertools import combinations_with_replacement


def go(x, turn, tree, cnt):
    if not tree[x]:
        cnt[x].append(turn)
        return
    child = tree[x][0]
    tree[x].rotate(-1)
    go(child, turn, tree, cnt)


def solution(edges, target):
    target = [0] + target
    N = len(edges) + 1
    tree = [[] for _ in range(N + 1)]
    for u, v in edges:
        tree[u].append(v)
    for n in range(1, N + 1):
        tree[n] = deque(sorted(tree[n]))

    cnt = [[] for _ in range(N + 1)]
    turn = 0
    while True:
        go(1, turn, tree, cnt)
        ok = True
        for i in range(1, N + 1):
            if target[i] > 3 * len(cnt[i]):
                ok = False
                break
            elif target[i] < len(cnt[i]):
                return [-1]
        if ok:
            break
        turn += 1
    ans = [0] * sum(map(lambda x: len(x), cnt))
    for n in range(1, N + 1):
        if not cnt[n]:
            continue
        for case in combinations_with_replacement(range(1, 4), r=len(cnt[n])):
            if sum(case) == target[n]:
                break
        for i, num in zip(cnt[n], sorted(case)):
            ans[i] = num
    return ans


print(
    solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]))
