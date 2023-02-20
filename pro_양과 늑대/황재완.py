# 풀이1: BFS with bitmasking
import heapq

ans = 0
node_list = None
visited = None
binary_tree = None


def go(n, info, visited):
    visited[n] = True
    cnt = [0, 0]  # sheep, wolf
    for v in binary_tree[n]:
        if not visited[v]:
            sc, wc = go(v, info, visited)
            cnt[0] += sc
            cnt[1] += wc
    node_list[n] = [info[n], -cnt[0], cnt[1], n]  # 양or늑대, 양개수, 늑대개수
    cnt[info[n]] += 1
    return cnt


def solution(info, edges):
    global ans, node_list, binary_tree
    binary_tree = [[] for _ in range(len(info))]
    node_list = [0] * len(info)
    for u, v in edges:
        binary_tree[u].append(v)
    go(0, info, [False] * len(info))

    ans = 0
    pq = []
    heapq.heappush(pq, node_list[0])
    visited = [False] * len(info)
    cnt = [0, 0]
    while pq:
        sheep_or_wolf, sheep_cnt, wolf_cnt, n = heapq.heappop(pq)
        ans += 1 - sheep_or_wolf
        cnt[sheep_or_wolf] += 1
        visited[n] = True
        if cnt[0] == cnt[1]:
            break
        for v in binary_tree[n]:
            if not visited[v]:
                heapq.heappush(pq, node_list[v])

    ans = cnt[0]
    return ans


from collections import deque


def solution(info, edges):
    N = len(info)
    binary_tree = [[] for _ in range(N)]
    d = [[[False] * N] for _ in range(N) for _ in range(N)]  # 노드번호, 양개수, 늑대개수
    for u, v in edges:
        binary_tree[u].append(v)
        binary_tree[v].append(u)
    q = deque([0, 1, 0])
    d[0][1][0] = True
    while q:
        n, s, w = q.popleft()
        for v in binary_tree[n]:
            if info[v] == 1:
                if s > w + 1 and not d[v][s][w + 1]:
                    d[v][s][w + 1] = True
                    q.append((v, s, w + 1))
                elif s + 1 > w and not d[v][s + 1][w]:
                    d[v][s + 1][w] = True
                    q.append((v, s + 1, w))
    ans = 0
    for n in range(N):
        for s in range(N):
            for w in range(0, s):
                if d[n][s][w]:
                    ans = max(ans, s)

    return ans


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
