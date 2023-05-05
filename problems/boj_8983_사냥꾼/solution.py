import sys
import bisect

sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N, L = map(int, input().split())
xs = list(map(int, input().split()))
xs.sort()
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    if y > L:
        continue
    p = bisect.bisect_left(xs, x)
    if p < len(xs) and abs(x - xs[p]) + y <= L:
        ans += 1
        continue
    if p - 1 >= 0 and abs(x - xs[p - 1]) + y <= L:
        ans += 1
        continue
print(ans)
