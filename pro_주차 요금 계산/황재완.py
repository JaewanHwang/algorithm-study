from collections import defaultdict
import math

def solution(fees, records):
    vcht, vtht, vhht = defaultdict(int), defaultdict(int), defaultdict(int)
    bm, bc, um, uc = fees
    LIMIT = 23 * 60 + 59

    for record in records:
        t, vn, o = record.split(' ')
        h, m = map(int, t.split(':'))
        t = h * 60 + m
        if o == 'IN':
            vhht[vn] = t
        else:
            vtht[vn] += t - vhht[vn]
            vhht[vn] = -1
    for vn in vhht:
        if vhht[vn] != -1:
            vtht[vn] += LIMIT - vhht[vn]
        vcht[vn] = bc
        diff = vtht[vn] - bm
        if diff > 0:
            vcht[vn] += uc * math.ceil(diff / um)

    ans = list(map(lambda x: x[1], sorted(vcht.items())))
    return ans