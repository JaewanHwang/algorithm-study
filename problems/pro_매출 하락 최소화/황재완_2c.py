def go(cur, attend, d, tree, sales):
    if d[cur][attend] != -1:
        return d[cur][attend]

    if attend == 0:
        min_diff = float('inf')
        attend_flag = False
        d[cur][attend] = 0
        for child in tree[cur]:
            res_attend = go(child, 1, d, tree, sales)
            res_not_attend = go(child, 0, d, tree, sales)
            if res_attend > res_not_attend and min_diff > res_attend - res_not_attend:
                min_diff = res_attend - res_not_attend
            if res_attend <= res_not_attend:
                attend_flag = True
                d[cur][attend] += res_attend
            else:
                d[cur][attend] += res_not_attend
        if tree[cur] and not attend_flag:
            d[cur][attend] += min_diff
    else:
        d[cur][attend] = sales[cur]
        for child in tree[cur]:
            d[cur][attend] += min(go(child, 0, d, tree, sales), go(child, 1, d, tree, sales))

    return d[cur][attend]


def solution(sales, links):
    sales = [0] + sales
    tree = [[] for _ in range(len(sales))]
    for u, v in links:
        tree[u].append(v)
    d = [[-1] * 2 for _ in range(len(sales))]
    ans = min(go(1, 0, d, tree, sales), go(1, 1, d, tree, sales))
    return ans