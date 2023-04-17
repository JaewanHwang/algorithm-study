# 풀이1: BFS with bitmasking



# 풀이 2: 상태를 기록하는 DFS
from collections import deque

ans = 0
binary_tree = None
info = None


def go(n, sheep_cnt, wolf_cnt, edge_set):
    global ans
    cur_edge_set = set(edge_set)
    cur_edge_set.remove(n)
    sheep_cnt += info[n] ^ 1
    wolf_cnt += info[n]
    if wolf_cnt >= sheep_cnt:
        return
    ans = max(ans, sheep_cnt)
    for v in binary_tree[n]:
        cur_edge_set.add(v)
    for v in cur_edge_set:
        go(v, sheep_cnt, wolf_cnt, cur_edge_set)


def solution(nodes, edges):
    global info, binary_tree
    info = nodes
    N = len(info)
    binary_tree = [[] for _ in range(N)]
    for u, v in edges:
        binary_tree[u].append(v)
    go(0, 0, 0, {0})
    return ans
