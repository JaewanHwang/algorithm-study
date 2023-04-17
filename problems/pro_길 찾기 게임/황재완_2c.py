from collections import defaultdict, deque


def go(num, i, levels, tree, l, r, ans, nodeinfo):
    ans[0].append(num)
    x, y = nodeinfo[num - 1]
    if i + 1 < len(levels):
        next_level = levels[i + 1]
        if tree[next_level] and l <= tree[next_level][-1][0] < x:
            _, child = tree[next_level].pop()
            go(child, i + 1, levels, tree, l, x - 1, ans, nodeinfo)
        if tree[next_level] and x < tree[next_level][-1][0] <= r:
            _, child = tree[next_level].pop()
            go(child, i + 1, levels, tree, x + 1, r, ans, nodeinfo)
    ans[1].append(num)


def solution(nodeinfo):
    tree = defaultdict(list)
    ans = [[], []]
    l, r = 10_000, 1
    for i, (x, y) in enumerate(nodeinfo, start=1):
        tree[y].append((x, i))
        l = min(l, x)
        r = max(r, x)
    for y in tree:
        tree[y].sort(reverse=True)
    levels = sorted(tree, reverse=True)
    root_y = levels[0]
    _, root_num = tree[root_y].pop()
    go(root_num, 0, levels, tree, l, r, ans, nodeinfo)
    return ans


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
