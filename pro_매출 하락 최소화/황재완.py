d = None
sum_child = None
tree = None


def go(n, attend, sales):
    if d[n][attend] != -1:
        return d[n][attend]
    if sum_child[n] == -1:
        sum_child[n] = 0
        for child in tree[n]:
            sum_child[n] += min(go(child, 0, sales), go(child, 1, sales))
    if attend == 1:
        d[n][1] = sales[n - 1] + sum_child[n]
    else:
        for child in tree[n]:
            if d[child][0] > d[child][1]:
                d[n][0] = sum_child[n]
                break
        else:
            d[n][0] = sum_child[n] + min(map(lambda child: d[child][1] - d[child][0], tree[n]))
    return d[n][attend]


def solution(sales, links):
    global d, sum_child, tree
    N = len(sales)
    tree = [[] for _ in range(N + 1)]
    d = [[-1] * 2 for _ in range(N + 1)]
    sum_child = [-1] * (N + 1)
    for x, y in links:
        tree[x].append(y)
    for x in range(1, N + 1):
        if not tree[x]:
            d[x][0] = 0
            d[x][1] = sales[x - 1]
            sum_child[x] = 0
    ans = min(go(1, 0, sales), go(1, 1, sales))
    return ans
