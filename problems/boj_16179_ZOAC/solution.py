import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

s = list(input().rstrip())
cnt = defaultdict(set)
for i in range(len(s)):
    cnt[s[i]].add(i)

ans = [''] * len(s)
for _ in range(len(s)):
    min_s, min_c, min_p = 'Z' * len(s), 0, 0
    for c in cnt:
        for p in cnt[c]:
            tmp = ans[p]
            ans[p] = c
            res = ''.join(ans)
            if min_s > res:
                min_s = res
                min_c = c
                min_p = p
            ans[p] = tmp
    print(min_s)
    ans[min_p] = min_c
    cnt[min_c].remove(min_p)
