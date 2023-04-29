import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
a.sort()
l, r, = 0, N - 1
cur = a[l] + a[r]
min_diff = float('inf')
while l < r and min_diff != 0:
    if 0 <= abs(cur) < min_diff:
        ans = [a[l], a[r]]
        min_diff = abs(cur)
    if cur < 0:
        cur -= a[l]
        l += 1
        cur += a[l]
    else:
        cur -= a[r]
        r -= 1
        cur += a[r]
print(*ans)
