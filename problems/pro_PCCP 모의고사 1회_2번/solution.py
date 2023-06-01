from itertools import permutations


def solution(ability):
    N, K = len(ability), len(ability[0])
    ans = 0
    for case in permutations(range(N), r=K):
        res = 0
        for k, n in enumerate(case):
            res += ability[n][k]
        ans = max(ans, res)
    return ans
