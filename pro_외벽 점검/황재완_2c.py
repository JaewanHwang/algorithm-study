from itertools import permutations


def go(start, dist, n, weak):
    w_idx = start
    d_idx = 0
    cur = start
    while d_idx < len(dist):
        end = weak[cur] + dist[d_idx]
        if (weak[cur] < weak[(w_idx + 1) % len(weak)] <= end) or (
                weak[(w_idx + 1) % len(weak)] < weak[cur] and end >= weak[(w_idx + 1) % len(weak)] + n):
            w_idx = (w_idx + 1) % len(weak)
        else:
            w_idx = (w_idx + 1) % len(weak)
            cur = w_idx
            d_idx += 1
        if w_idx == start:
            return True
    return False


def solution(n, weak, dist):
    if max(dist) >= n:
        return 1
    for ans in range(1, len(dist) + 1):
        for start in range(len(weak)):
            for case in permutations(dist, r=ans):
                if go(start, case, n, weak):
                    return ans
    if ans == len(dist):
        return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
