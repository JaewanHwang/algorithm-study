import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")


def check():
    for y in range(W):
        last, cnt = -1, 0
        ok = False
        for x in range(D):
            if m[x][y] == last:
                cnt += 1
            else:
                cnt = 1
                last = m[x][y]
            if cnt >= K:
                ok = True
                break
        if not ok:
            return False
    return True


def go(i, case):
    if i == len(case):
        if check():
            return True
        return False

    original_row = m[case[i]][:]
    for c in range(2):
        m[case[i]] = [c] * W
        if go(i + 1, case):
            return True
        m[case[i]] = original_row
    return False


T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(D)]
    ok = False
    max_cons = [0] * W
    for ans in range(0, D):
        for case in combinations(range(D), r=ans):
            if go(0, case):
                ok = True
                break
        if ok:
            break
    else:
        ans = D
    print(f'#{test_case} {ans}')
