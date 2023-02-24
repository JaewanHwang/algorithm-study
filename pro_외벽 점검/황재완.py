from itertools import permutations


def go(start, dist, weak):
    d_idx, w_idx, cur = 0, start, start
    while d_idx < len(dist):
        d = weak[w_idx] - weak[cur] if weak[cur] <= weak[w_idx] else N - (weak[cur] - weak[w_idx])

        if d < dist[d_idx]:
            w_idx = (w_idx + 1) % W
        else:
            if d == dist[d_idx]:
                w_idx = (w_idx + 1) % W
            d_idx += 1
            cur = w_idx

        if w_idx == start:
            return True

    return False


D, W, N = 0, 0, 0


def solution(n, weak, dist):
    global D, W, N
    W, D, N = len(weak), len(dist), n

    for r in range(1, D + 1):
        for case in permutations(dist, r=r):
            for start in range(W):
                if go(start, case, weak):
                    return r
    return -1
