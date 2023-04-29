import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = (s[i - 1] + a[i]) % M

cnt = defaultdict(int)
cnt[0] = 1
ans = 0
for j in range(1, N + 1):
    ans += cnt[s[j]]
    cnt[s[j]] += 1
print(ans)
