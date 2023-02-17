import sys

sys.setrecursionlimit(10 ** 6)
ans = [[], []]
x_sorted_nodes = []


def go(l, r, nodeinfo):
    if l > r:
        return
    cur_node_index = max(range(l, r + 1), key=lambda x: x_sorted_nodes[x][1])
    x, y, cur_node = x_sorted_nodes[cur_node_index]

    ans[0].append(cur_node)

    # left subtree
    go(l, cur_node_index - 1, nodeinfo)
    # right subtree
    go(cur_node_index + 1, r, nodeinfo)

    ans[1].append(cur_node)


def solution(nodeinfo):
    global x_sorted_nodes

    for num, node in enumerate(nodeinfo):
        x, y = node
        x_sorted_nodes.append((x, y, num + 1))
    x_sorted_nodes.sort()

    go(0, len(nodeinfo) - 1, nodeinfo)
    return ans


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
