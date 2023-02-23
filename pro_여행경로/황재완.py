from collections import defaultdict


def go(n, start):
    global ans
    path[n] = start
    if n == N:
        if ans > path:
            ans = path[:]
        return
    for i in range(len(adj_list[start])):
        if not visited[start][i]:
            visited[start][i] = True
            go(n + 1, adj_list[start][i])
            visited[start][i] = False


ans = None
N = 0
visited = None
airport_name_list = None
path = None
adj_list = None


def solution(tickets):
    global ans, N, visited, path, adj_list
    N = len(tickets)
    path = [0] * (N + 1)
    airport_set = set()
    adj_list = defaultdict(list)
    visited = dict()

    for start, dest in tickets:
        adj_list[start].append(dest)
        airport_set.add(start)
        airport_set.add(dest)

    for start in adj_list:
        visited[start] = [False] * len(adj_list[start])
    ans = ['ZZZ'] * (N + 1)

    go(0, 'ICN')
    return ans
