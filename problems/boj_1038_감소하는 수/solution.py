import sys
from itertools import combinations
from functools import reduce

sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())

ans = []

for r in range(1, 11):
    for case in combinations(range(10), r=r):
        ans.append(reduce(lambda x, y: 10 * x + y, sorted(case, reverse=True)))
ans.sort()
if N >= len(ans):
    print(-1)
else:
    print(ans[N])
