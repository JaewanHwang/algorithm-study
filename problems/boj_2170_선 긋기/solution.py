import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], x[1]))
x, y = arr[0]
pq = [(-y, x)]
for x, y in arr[1:]:
    cy, cx = heappop(pq)
    cy = -cy
    if x > cy:
        heappush(pq, (-cy, cx))
        heappush(pq, (-y, x))
    else:
        nx = min(cx, x)
        ny = max(cy, y)
        heappush(pq, (-ny, nx))
ans = 0
for y, x in pq:
    ans += -y - x
print(ans)
