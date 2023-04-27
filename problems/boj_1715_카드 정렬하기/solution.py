import sys
import heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))
if len(arr) == 1:
    print(0)
    sys.exit(0)

ans = 0
pq = arr
heapq.heapify(pq)
while len(pq) > 1:
    x, y = heapq.heappop(pq), heapq.heappop(pq)
    ans += x + y
    heapq.heappush(pq, x + y)

print(ans)
