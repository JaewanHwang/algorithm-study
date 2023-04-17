import sys
from itertools import permutations
from collections import deque

sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
original_m = [list(map(int, input().split())) for _ in range(N)]
op = []
for _ in range(K):
    r, c, s = map(int, input().split())
    op.append((r - 1, c - 1, s))
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)


def go(sx, sy, l, q, is_insert, m):
    for y in range(sy - l, sy + l + 1):
        if is_insert:
            m[sx - l][y] = q.popleft()
        else:
            q.append(m[sx - l][y])
    for x in range(sx - l + 1, sx + l + 1):
        if is_insert:
            m[x][sy + l] = q.popleft()
        else:
            q.append(m[x][sy + l])
    for y in range(sy + l - 1, sy - l - 1, -1):
        if is_insert:
            m[sx + l][y] = q.popleft()
        else:
            q.append(m[sx + l][y])

    for x in range(sx + l - 1, sx - l, -1):
        if is_insert:
            m[x][sy - l] = q.popleft()
        else:
            q.append(m[x][sy - l])


def simulate(case):
    global ans
    m = [row[:] for row in original_m]
    for x, y, s in case:
        for l in range(s, 0, -1):
            q = deque()
            go(x, y, l, q, False, m)
            q.rotate(1)
            go(x, y, l, q, True, m)
    ans = min(ans, min(sum(row) for row in m))


ans = float('inf')
for case in set(permutations(op)):
    simulate(case)
print(ans)
