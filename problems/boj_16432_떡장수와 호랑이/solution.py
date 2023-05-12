import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
a = []
d = [[0] * 10 for _ in range(N)]
for _ in range(N):
    m, *b = map(int, input().split())
    a.append(b)
q = deque(map(lambda x: (x, 0), a[0]))
while q:
    cur, today = q.popleft()
    if today == N - 1:
        ans = [cur]
        while d[today][cur]:
            cur, today = d[today][cur], today - 1
            ans.append(cur)
        print(*ans[::-1], sep='\n')
        sys.exit(0)
    for nxt in a[today + 1]:
        if nxt == cur:
            continue
        if not d[today + 1][nxt]:
            d[today + 1][nxt] = cur
            q.append((nxt, today + 1))
print(-1)
