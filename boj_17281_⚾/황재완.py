import sys
from itertools import permutations

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
record = [list(map(int, input().split())) for _ in range(N)]


def simulate(case):
    res = 0
    order = list(case)
    order.insert(3, 0)
    p = 0
    for inning in range(N):
        out_cnt = 0
        base = [0] * 4
        while out_cnt < 3:
            cur = record[inning][order[p]]
            if cur == 1:
                res += base[3]
                base[3], base[2], base[1] = base[2], base[1], 1
            elif cur == 2:
                res += base[2] + base[3]
                base[3], base[2], base[1] = base[1], 1, 0
            elif cur == 3:
                res += base[1] + base[2] + base[3]
                base[3], base[2], base[1] = 1, 0, 0
            elif cur == 4:
                res += base[1] + base[2] + base[3] + 1
                base[3], base[2], base[1] = 0, 0, 0
            else:
                out_cnt += 1
            p = (p + 1) % 9
    return res


ans = 0
for case in permutations(range(1, 9), r=8):
    ans = max(ans, simulate(case))
print(ans)
