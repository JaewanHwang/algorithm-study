# 풀이2: 효율성 테스트 통과 (카카오 해설 풀이)
import sys

sys.setrecursionlimit(10 ** 6)


def evaluate(root, num, mid, links):
    dp = [[-1] * 2 for _ in range(len(num))]
    go(root, 0, dp, links, mid, num)
    return dp[root][0]


def go(v, k, dp, links, L, num):
    if v == -1:
        if k == 0:
            return 1
        elif k == 1:
            return 0

    if dp[v][k] != -1:
        return dp[v][k]
    dpi1 = go(links[v][0], 1, dp, links, L, num)
    dpj1 = go(links[v][1], 1, dp, links, L, num)
    dpi0 = go(links[v][0], 0, dp, links, L, num)
    dpj0 = go(links[v][1], 0, dp, links, L, num)

    if num[v] + dpi1 + dpj1 <= L:
        if k == 0:
            dp[v][0] = dpi0 + dpj0 - 1
        else:
            dp[v][1] = num[v] + dpi1 + dpj1
    elif num[v] + dpi1 <= L or num[v] + dpj1 <= L:
        if k == 0:
            dp[v][0] = dpi0 + dpj0
        else:
            dp[v][1] = num[v] + min(dpi1, dpj1)
    elif num[v] <= L:
        if k == 0:
            dp[v][0] = dpi0 + dpj0 + 1
        else:
            dp[v][1] = num[v]
    else:
        dp[v][k] = float('inf')

    return dp[v][k]


def solution(k, num, links):
    # root를 찾는다.
    in_degree = [0] * len(num)
    for i, (l, r) in enumerate(links):
        if l != -1:
            in_degree[l] += 1
        if r != -1:
            in_degree[r] += 1
    if len(num) == 1:
        root = 0
    else:
        for i in range(len(num)):
            if in_degree[i] == 0 and (links[i][0] != -1 or links[i][1] != -1):
                root = i
                break

    max_num = max(num)
    l, r = max_num, 10000 * 10000
    while l <= r:
        mid = (l + r) // 2
        if evaluate(root, num, mid, links) <= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans


print(solution(3,
               [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
               [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1],
                [-1, -1]]
               ))
