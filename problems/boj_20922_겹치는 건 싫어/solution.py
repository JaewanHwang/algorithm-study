import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))
l, r = 0, -1
cur = defaultdict(int)
ans = 0
while l < N and r < N:
    if r + 1 < N and cur[a[r + 1]] + 1 <= K:
        r += 1
        cur[a[r]] += 1
        ans = max(ans, r - l + 1)
    else:
        cur[a[l]] -= 1
        l += 1
print(ans)
