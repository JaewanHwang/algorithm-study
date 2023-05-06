import sys
from collections import Counter

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, B = map(int, input().split())
m = []
for _ in range(N):
    m.extend(list(map(int, input().split())))
m = Counter(m)
hs = sorted(m, reverse=True)
ans_t, ans_h = float('inf'), 0
for pivot in range(hs[0], hs[-1] - 1, -1):
    res = 0
    cur = B
    ok = True
    for h in hs:
        if h > pivot:
            cur += (h - pivot) * m[h]
            res += (h - pivot) * 2 * m[h]
        elif h < pivot:
            if cur < (pivot - h) * m[h]:
                ok = False
                break
            cur -= (pivot - h) * m[h]
            res += (pivot - h) * m[h]
    if ok:
        if res < ans_t:
            ans_t = res
            ans_h = pivot
print(ans_t, ans_h)
