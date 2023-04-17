from collections import deque


def go1(cur, next, s, q, d, w):
    if d[next][s] == -1 or d[next][s] > d[cur][s] + w >= 0:
        d[next][s] = d[cur][s] + w
        q.append((next, s))


def go2(cur, next, s, q, d, w, trap2index):
    ns = s ^ 1 << trap2index[next]
    if d[next][ns] == -1 or d[next][ns] > d[cur][s] + w >= 0:
        d[next][ns] = d[cur][s] + w
        q.append((next, ns))


def solution(n, start, end, roads, traps):
    trap2index = {t: i for i, t in enumerate(traps)}
    in_degrees, out_degrees = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
    for P, Q, S in roads:
        in_degrees[Q].append((P, S))
        out_degrees[P].append((Q, S))
    d = [[-1] * (2 ** len(traps)) for _ in range(n + 1)]
    d[start][0] = 0
    q = deque([(start, 0)])
    while q:
        cur, s = q.popleft()
        if cur not in trap2index:
            for next, w in out_degrees[cur]:
                if next not in trap2index:
                    go1(cur, next, s, q, d, w)
                elif next in trap2index and not s & 1 << trap2index[next]:
                    go2(cur, next, s, q, d, w, trap2index)
            for next, w in in_degrees[cur]:
                if next in trap2index and s & 1 << trap2index[next]:
                    go2(cur, next, s, q, d, w, trap2index)
        else:
            for next, w in out_degrees[cur]:
                if not s & 1 << trap2index[cur] and next in trap2index and not s & 1 << trap2index[next]:
                    go2(cur, next, s, q, d, w, trap2index)
                elif s & 1 << trap2index[cur] and next in trap2index and s & 1 << trap2index[next]:
                    go2(cur, next, s, q, d, w, trap2index)
                elif not s & 1 << trap2index[cur] and next not in trap2index:
                    go1(cur, next, s, q, d, w)
            for next, w in in_degrees[cur]:
                if s & 1 << trap2index[cur] and next in trap2index and not s & 1 << trap2index[next]:
                    go2(cur, next, s, q, d, w, trap2index)
                elif not s & 1 << trap2index[cur] and next in trap2index and s & 1 << trap2index[next]:
                    go2(cur, next, s, q, d, w, trap2index)
                elif s & 1 << trap2index[cur] and next not in trap2index:
                    go1(cur, next, s, q, d, w)
    ans = min(filter(lambda x: x != -1, d[end]))
    return ans
