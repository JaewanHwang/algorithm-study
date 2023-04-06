import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    m = dict()
    ans = 0
    for _ in range(N):
        x, y, d, K = map(int, input().split())
        m[(2 * x, 2 * y)] = [d, K]
    for _ in range(4001):
        tm = defaultdict(list)
        for (x, y), [d, p] in m.items():
            nx, ny = x + dx[d], y + dy[d]
            tm[(nx, ny)].append((d, p))
        for key in list(tm):
            if len(tm[key]) >= 2:
                ans += sum(p for _, p in tm[key])
                tm.pop(key)
            else:
                tm[key] = tm[key][0]
        m = tm
    print(f'#{test_case} {ans}')
