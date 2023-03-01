# 풀이1 Top-down

import sys

sys.setrecursionlimit(10 ** 6)


def go(i, first, d, money):
    if d[i][first] != -1:
        return d[i][first]
    d[i][first] = max(money[i] + go(i - 2, first, d, money),
                      go(i - 1, first, d, money))
    return d[i][first]


def solution(money):
    N = len(money)
    d = [[-1] * 2 for _ in range(N)]
    d[0][0] = 0
    d[0][1] = money[0]
    d[1][1] = money[0]
    d[1][0] = money[1]
    ans = max(money[N - 1] + go(N - 3, 0, d, money), go(N - 2, 1, d, money))
    return ans


# 풀이2 Bottom-up

def solution(money):
    N = len(money)
    d = [[-1] * 2 for _ in range(N)]
    d[0][0] = 0
    d[0][1] = money[0]
    d[1][1] = money[0]
    d[1][0] = money[1]

    for first in (0, 1):
        for i in range(2, N - 1):
            d[i][first] = max(d[i - 2][first] + money[i], d[i - 1][first])
    ans = max(money[N - 1] + d[N - 3][0], d[N - 2][1])
    return ans
