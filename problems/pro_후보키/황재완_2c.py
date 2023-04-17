from itertools import combinations


def solution(relation):
    R, C = len(relation), len(relation[0])
    all_key = []
    for l in range(1, C + 1):
        for case in combinations(range(C), r=l):
            all_key.append(sorted(case))

    super_key = set()
    for key in all_key:
        domain = set()
        for r in range(R):
            res = tuple(relation[r][c] for c in key)
            if res in domain:
                break
            domain.add(res)
        else:
            super_key.add(tuple(key))

    ans = 0
    for cur in sorted(super_key, key=lambda x: len(x)):
        if cur not in super_key:
            continue
        ans += 1
        cur = set(cur)
        for key in list(super_key):
            if cur <= set(key):
                super_key.remove(key)
    return ans
