import sys
import heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
cw = list(map(int, input().split()))
M = int(input())
bw = list(map(int, input().split()))
bw.sort()
if bw[-1] > max(cw):
    print(-1)
    sys.exit(0)

pqs = [[] for _ in range(N)]
for ci, c in enumerate(cw):
    for bi, b in enumerate(bw):
        if c - b < 0:
            break
        heapq.heappush(pqs[ci], (c - b, bi))
moved = [False] * M
ans = 0
cnt = 0
while cnt < M:
    ans += 1
    for ci in range(N):
        while pqs[ci]:
            _, now = heapq.heappop(pqs[ci])
            if not moved[now]:
                moved[now] = True
                cnt += 1
                break
print(ans)
