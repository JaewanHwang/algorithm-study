def solution(alp, cop, problems):
    max_alp_req, max_cop_req = 0, 0
    for alp_req, cop_req, _, _, _, in problems:
        max_alp_req, max_cop_req = max(max_alp_req, alp_req), max(max_cop_req, cop_req)
    alp, cop = min(alp, max_alp_req), min(cop, max_cop_req)
    d = [[float('inf')] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]
    d[alp][cop] = 0

    for a in range(alp + 1, max_alp_req + 1):
        for c in range(cop, max_cop_req + 1):
            d[a][c] = min(d[a][c], d[a - 1][c] + 1)

    for a in range(alp, max_alp_req + 1):
        for c in range(cop + 1, max_cop_req + 1):
            d[a][c] = min(d[a][c], d[a][c - 1] + 1)

    for a in range(alp, max_alp_req + 1):
        for c in range(cop, max_cop_req + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    na, nc = min(max_alp_req, a + alp_rwd), min(max_cop_req, c + cop_rwd)
                    d[na][nc] = min(d[na][nc], d[a][c] + cost)

    ans = d[max_alp_req][max_cop_req]
    return ans


print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
