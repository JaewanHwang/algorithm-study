import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")


def evaluate(m):
    for y in range(W):
        cur, cnt = m[0][y], 1
        for x in range(D):
            if x == 0:
                cur, cnt = m[x][y], 1
            else:
                if m[x][y] == cur:
                    cnt += 1
                else:
                    cur, cnt = m[x][y], 1
            if cnt >= K:
                break
        else:
            return False
    return True


def ok(case):
    for flag in range(2 ** len(case)):
        for i in range(len(case)):
            m[case[i]] = b_film if flag & 1 << i else a_film
        if evaluate(m):
            return True
    for l in case:
        m[l] = original_m[l]
    return False


T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(D)]
    original_m = [row[:] for row in m]
    a_film, b_film = [0] * W, [1] * W
    for ans in range(D):
        for case in combinations(range(D), r=ans):
            if ok(case):
                break
        else:
            continue
        break
    else:
        ans = D
    print(f'#{test_case} {ans}')
