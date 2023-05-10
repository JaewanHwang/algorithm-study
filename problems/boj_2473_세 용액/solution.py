import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
a = sorted(map(int, input().split()))
min_diff, min_case = float('inf'), None
for m in range(N - 2):
    l, r = m + 1, N - 1
    cur = a[l] + a[r] + a[m]
    while l < r:
        if abs(cur) < min_diff:
            min_diff = abs(cur)
            min_case = a[l], a[r], a[m]
        if cur > 0:
            cur -= a[r]
            r -= 1
            cur += a[r]
        else:
            cur -= a[l]
            l += 1
            cur += a[l]

print(*sorted(min_case))
