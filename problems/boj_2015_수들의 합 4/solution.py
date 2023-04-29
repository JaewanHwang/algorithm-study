import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    a[i] = a[i - 1] + a[i]
ans = 0
cnt = defaultdict(int)
cnt[0] = 1
for i in range(1, N + 1):
    ans += cnt[a[i] - K]
    cnt[a[i]] += 1

print(ans)
