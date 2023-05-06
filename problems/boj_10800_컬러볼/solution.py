import sys
from collections import defaultdict
import bisect

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
a = defaultdict(lambda: [0])
line = [0]
color = []
for _ in range(N):
    c, s = map(int, input().split())
    color.append((c, s))
    line.append(s)
    a[c].append(s)

sa = dict()
for c in a:
    a[c].sort()
    sa[c] = [0] * len(a[c])
    for i in range(1, len(a[c])):
        sa[c][i] = sa[c][i - 1] + a[c][i]

line.sort()
sl = [0] * (N + 1)
for i in range(1, N + 1):
    sl[i] = sl[i - 1] + line[i]

ans = []
for c, s in color:
    ans.append(sl[bisect.bisect_left(line, s) - 1] - sa[c][bisect.bisect_left(a[c], s) - 1])

print(*ans, sep='\n')
