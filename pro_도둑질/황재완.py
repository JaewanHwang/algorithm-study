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


print(solution([1, 2, 3, 1]))
