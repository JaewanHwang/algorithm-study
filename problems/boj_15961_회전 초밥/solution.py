import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(N)]
l, r = 0, k - 1
s = defaultdict(int)
for i in range(k):
    s[a[i]] += 1
ans = len(s) + (0 if c in s else 1)
s[a[l]] -= 1
if s[a[l]] == 0:
    s.pop(a[l])
l = (l + 1) % N
r = (r + 1) % N
s[a[r]] += 1
while l > 0:
    ans = max(ans, len(s) + (0 if c in s else 1))
    s[a[l]] -= 1
    if s[a[l]] == 0:
        s.pop(a[l])
    l = (l + 1) % N
    r = (r + 1) % N
    s[a[r]] += 1
print(ans)
