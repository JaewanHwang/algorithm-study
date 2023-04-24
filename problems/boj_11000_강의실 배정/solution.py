import sys
import heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
timetable = sorted(tuple(map(int, input().split())) for _ in range(N))
pq = []
heapq.heappush(pq, 0)
for s, t in timetable:
    now = heapq.heappop(pq)
    if now <= s:
        heapq.heappush(pq, t)
    else:
        heapq.heappush(pq, now)
        heapq.heappush(pq, t)

print(len(pq))
