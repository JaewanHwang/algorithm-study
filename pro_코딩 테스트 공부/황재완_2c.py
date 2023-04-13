def solution(alp, cop, problems):
    max_alp, max_cop = alp, cop
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp, max_cop = max(max_alp, alp_req), max(max_cop, cop_req)
    d = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    for i in range(alp + 1):
        for j in range(cop + 1):
            d[i][j] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i + 1 <= max_alp:
                    d[i + 1][j] = min(d[i + 1][j], d[i][j] + 1)
                if j + 1 <= max_cop:
                    d[i][j + 1] = min(d[i][j + 1], d[i][j] + 1)
                if i >= alp_req and j >= cop_req:
                    d[min(max_alp, i + alp_rwd)][min(max_cop, j + cop_rwd)] = min(
                        d[min(max_alp, i + alp_rwd)][min(max_cop, j + cop_rwd)], d[i][j] + cost)
    ans = d[max_alp][max_cop]
    return ans
