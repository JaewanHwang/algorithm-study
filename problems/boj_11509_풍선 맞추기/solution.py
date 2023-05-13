import sys
from collections import defaultdict
import bisect

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
h_map = defaultdict(list)
for i, h in enumerate(H):
    h_map[h].append(i)

heights = sorted(h_map, reverse=True)
i = 0
ans = 0
while i < len(heights):
    ans += 1
    h = heights[i]
    cur = 0
    while True:
        if h in h_map:
            pos = bisect.bisect_left(h_map[h], cur)
            if pos < len(h_map[h]):
                cur = h_map[h][pos]
                h_map[h].remove(h_map[h][pos])
                if not h_map[h]:
                    h_map.pop(h)
                h -= 1
            else:
                break
        else:
            break
    while i < len(heights) and heights[i] not in h_map:
        i += 1
print(ans)
