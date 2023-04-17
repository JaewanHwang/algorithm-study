def go(n, candidates, adj_list, s, w, info):
    candidates.remove(n)
    s += 1 ^ info[n]
    w += 0 ^ info[n]
    for v in adj_list[n]:
        candidates.add(v)
    res = s
    for next in candidates:
        if (info[next] ^ 1) + s > (info[next] ^ 0) + w:
            res = max(res, go(next, set(candidates), adj_list, s, w, info))
    return res


def solution(info, edges):
    adj_list = [[] for _ in range(len(info))]
    for p, c in edges:
        adj_list[p].append(c)
    ans = go(0, {0}, adj_list, 0, 0, info)
    return ans


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
