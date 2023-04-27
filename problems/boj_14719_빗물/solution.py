import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
H, W = map(int, input().split())
heights = list(map(int, input().split()))

l_max = [0] * W
l_max[0] = heights[0]
r_max = [0] * W
r_max[-1] = heights[-1]
for i in range(1, W):
    l_max[i] = max(l_max[i - 1], heights[i])
    r_max[W - i - 1] = max(r_max[W - i], heights[W - i - 1])

ans = 0
for i in range(1, W - 1):
    ans += max(min(l_max[i - 1], r_max[i + 1]) - heights[i], 0)
print(ans)
