from itertools import chain


def solution(land, P, Q):
    line = list(chain.from_iterable(land))
    line.sort()

    N = len(line)

    ans = cost = (sum(line) - line[0] * N) * Q

    for i in range(1, N):
        if line[i] != line[i - 1]:
            cost += (line[i] - line[i - 1]) * i * P - (line[i] - line[i - 1]) * (N - i) * Q
            if ans < cost:
                break
            ans = min(ans, cost)
    return ans


print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3))
