def solution(n, s, a, b, fares):
    adj_mat = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        adj_mat[i][i] = 0
    for u, v, c in fares:
        adj_mat[u][v] = adj_mat[v][u] = c
    for k in range(1, n + 1):
        for u in range(1, n + 1):
            for v in range(1, n + 1):
                adj_mat[u][v] = min(adj_mat[u][v], adj_mat[u][k] + adj_mat[k][v])
    ans = float('inf')
    for i in range(1, n + 1):
        ans = min(ans, adj_mat[s][i] + adj_mat[i][a] + adj_mat[i][b])
    return ans
