import sys

sys.setrecursionlimit(10 ** 6)


def go(dp, v, num, links, L):
    if dp[v][0] != -1:
        return False
    i, j = links[v]
    if go(dp, i, num, links, L):
        return True
    if go(dp, j, num, links, L):
        return True

    if num[v] + dp[i][1] + dp[j][1] <= L:
        dp[v][0] = dp[i][0] + dp[j][0] - 1
        dp[v][1] = num[v] + dp[i][1] + dp[j][1]
    elif num[v] + dp[i][1] <= L or num[v] + dp[j][1] <= L:
        dp[v][0] = dp[i][0] + dp[j][0]
        dp[v][1] = num[v] + min(dp[i][1], dp[j][1])
    elif num[v] <= L:
        dp[v][0] = dp[i][0] + dp[j][0] + 1
        dp[v][1] = num[v]
    else:
        return True
    return False


def ok(dp, root, k, num, links, L):
    if go(dp, root, num, links, L):
        return False
    if dp[root][0] <= k:
        return True
    return False


def solution(k, num, links):
    l = sum(num) // len(num)
    r = sum(num)
    in_degree = [0] * len(num)
    for left, right in links:
        if left != -1:
            in_degree[left] += 1
        if right != -1:
            in_degree[right] += 1

    for i in range(len(num)):
        if in_degree[i] == 0:
            root = i
            break
    ans = 0
    while l <= r:
        L = (l + r) // 2
        dp = [[-1] * 2 for _ in range(len(num) + 1)]
        dp[-1] = [1, 0]
        if ok(dp, root, k, num, links, L):
            ans = L
            r = L - 1
        else:
            l = L + 1
    return ans


print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
               [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1],
                [-1, -1]]))
