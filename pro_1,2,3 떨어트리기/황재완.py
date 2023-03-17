from collections import deque, defaultdict


def find_order(n, tree):
    if not tree[n]:
        return n
    child = tree[n].popleft()
    tree[n].append(child)
    return find_order(child, tree)


def solution(edges, target):
    N = len(edges) + 1
    tree = [[] for _ in range(N + 1)]
    for p, c in edges:
        tree[p].append(c)
    leaf_nodes = []
    for i in range(1, N + 1):
        if not tree[i]:
            leaf_nodes.append(i)
        else:
            tree[i] = deque(sorted(tree[i]))

    counter_leaf_node = defaultdict(list)
    k = 0
    while True:
        counter_leaf_node[find_order(1, tree)].append(k)
        impossible, keep_going = False, False
        for leaf_node in leaf_nodes:
            if target[leaf_node - 1] > len(counter_leaf_node[leaf_node]) * 3:
                keep_going = True
                break
            elif target[leaf_node - 1] < len(counter_leaf_node[leaf_node]):
                impossible = True
                break
        if impossible:
            return [-1]
        elif keep_going:
            k += 1
        else:
            break

    sum_map = [[0] * 101 for _ in range(101)]
    for one_cnt in range(101):
        for two_cnt in range(51):
            for three_cnt in range(34):
                tot_sum = one_cnt + two_cnt * 2 + three_cnt * 3
                tot_cnt = one_cnt + two_cnt + three_cnt
                if tot_sum <= 100:
                    if not sum_map[tot_cnt][tot_sum] or sum_map[tot_cnt][tot_sum] < (one_cnt, two_cnt, three_cnt):
                        sum_map[tot_cnt][tot_sum] = (one_cnt, two_cnt, three_cnt)

    ans = [0] * (k + 1)
    for leaf_node in counter_leaf_node:
        if counter_leaf_node[leaf_node]:
            now_best = sum_map[len(counter_leaf_node[leaf_node])][target[leaf_node - 1]]
        else:
            continue
        now_best = [1] * now_best[0] + [2] * now_best[1] + [3] * now_best[2]
        for ni, ai in enumerate(counter_leaf_node[leaf_node]):
            ans[ai] = now_best[ni]
    return ans


print(solution(
    [[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]],
    [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
))
