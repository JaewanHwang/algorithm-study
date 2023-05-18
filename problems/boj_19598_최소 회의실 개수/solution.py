import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
a = [tuple(map(int, input().split())) for _ in range(N)]
pq = [0]
for s, e in sorted(a):
    cur = heappop(pq)
    if s >= cur:
        heappush(pq, e)
    else:
        heappush(pq, cur)
        heappush(pq, e)
print(len(pq))
