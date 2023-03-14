from collections import deque


def solution(n, start, end, roads, traps):
    d = [[-1] * (2 ** len(traps)) for _ in range(n + 1)]
    trap_map = dict()
    traps = set(traps)
    for i, trap in enumerate(traps):
        trap_map[trap] = i
    adj_mat = [[3000] * (n + 1) for _ in range(n + 1)]
    out_graph = [set() for _ in range(n + 1)]
    in_graph = [set() for _ in range(n + 1)]
    for x, y, c in roads:
        adj_mat[x][y] = min(adj_mat[x][y], c)
        out_graph[x].add(y)
        in_graph[y].add(x)

    d[start][0] = 0
    q = deque([(start, 0)])

    while q:
        x, s = q.popleft()
        if x not in traps:
            for y in out_graph[x]:
                if y not in traps:
                    if d[y][s] == -1 or d[y][s] > d[x][s] + adj_mat[x][y]:
                        d[y][s] = d[x][s] + adj_mat[x][y]
                        q.append((y, s))
                elif not s & 1 << trap_map[y]:
                    ns = s | 1 << trap_map[y]
                    if d[y][ns] == -1 or d[y][ns] > d[x][s] + adj_mat[x][y]:
                        d[y][ns] = d[x][s] + adj_mat[x][y]
                        q.append((y, ns))
            for y in in_graph[x]:
                if y in traps and s & 1 << trap_map[y]:
                    ns = s ^ 1 << trap_map[y]
                    if d[y][ns] == -1 or d[y][ns] > d[x][s] + adj_mat[y][x]:
                        d[y][ns] = d[x][s] + adj_mat[y][x]
                        q.append((y, ns))
        else:
            if not s & 1 << trap_map[x]:
                for y in out_graph[x]:
                    if y not in traps:
                        if d[y][s] == -1 or d[y][s] > d[x][s] + adj_mat[x][y]:
                            d[y][s] = d[x][s] + adj_mat[x][y]
                            q.append((y, s))
                    elif y in traps and not s & 1 << trap_map[y]:
                        ns = s | 1 << trap_map[y]
                        if d[y][ns] == -1 or d[y][ns] > d[x][s] + adj_mat[x][y]:
                            d[y][ns] = d[x][s] + adj_mat[x][y]
                            q.append((y, ns))
                for y in in_graph[x]:
                    if y in traps and s & 1 << trap_map[y]:
                        ns = s ^ 1 << trap_map[y]
                        if d[y][ns] == -1 or d[y][ns] > d[x][s] + adj_mat[y][x]:
                            d[y][ns] = d[x][s] + adj_mat[y][x]
                            q.append((y, ns))
            else:
                for y in in_graph[x]:
                    if y not in traps:
                        if d[y][s] == -1 or d[y][s] > d[x][s] + adj_mat[y][x]:
                            d[y][s] = d[x][s] + adj_mat[y][x]
                            q.append((y, s))
                    elif y in traps:
                        if not s & 1 << trap_map[y]:
                            ns = s | 1 << trap_map[y]
                            if d[y][ns] == -1 or d[y][ns] > d[x][s] + adj_mat[y][x]:
                                d[y][ns] = d[x][s] + adj_mat[y][x]
                                q.append((y, ns))
                for y in out_graph[x]:
                    if y in traps and s & 1 << trap_map[y]:
                        ns = s ^ 1 << trap_map[y]
                        if d[y][ns] == -1 or d[y][ns] > d[x][s] + adj_mat[x][y]:
                            d[y][ns] = d[x][s] + adj_mat[x][y]
                            q.append((y, ns))

    ans = -1
    for s in range(2 ** len(traps)):
        if ans == -1 or 0 < d[end][s] < ans:
            ans = d[end][s]
    return ans


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
