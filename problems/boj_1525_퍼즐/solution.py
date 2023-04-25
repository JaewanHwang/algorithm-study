import sys
from collections import deque, defaultdict
from itertools import chain
from functools import reduce

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
m = [list(map(lambda x: int(x) if x != '0' else 9, input().split())) for _ in range(3)]
start = str(reduce(lambda x, y: 10 * x + y, chain.from_iterable(m), 0))
d = defaultdict(lambda: -1)
d[start] = 0
TARGET = '123456789'
q = deque([(start, start.index('9'))])
while q:
    cur, pos = q.popleft()
    if cur == TARGET:
        break
    x, y = pos // 3, pos % 3
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 3 and 0 <= ny < 3:
            idx = nx * 3 + ny
            next = list(cur)
            next[idx], next[pos] = next[pos], next[idx]
            next = ''.join(next)
            if d[next] == -1:
                d[next] = d[cur] + 1
                q.append((next, idx))

ans = d[TARGET]
print(ans)
