def solution(n, s, a, b, fares):
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for c, d, f in fares:
        dist[c][d] = dist[d][c] = f
    for k in range(1, n + 1):
        for u in range(1, n + 1):
            for v in range(1, n + 1):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
    ans = float('inf')
    for m in range(1, n + 1):
        ans = min(ans, dist[s][m] + dist[m][b] + dist[m][a])
    return ans