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
    tm = [row[:] for row in m]
    for flag in range(2 ** len(case)):
        for i in range(len(case)):
            tm[case[i]] = [1 if flag & 1 << i else 0] * W
        if evaluate(tm):
            return True
    return False


T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(D)]
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
