import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    m = defaultdict(list)
    for _ in range(N):
        x, y, d, K = map(int, input().split())
        m[(2 * x, 2 * y)].append((d, K))
    ans = 0
    for _ in range(4000):
        tm = defaultdict(list)
        for (x, y), [(d, K)] in m.items():
            nx, ny = x + dx[d], y + dy[d],
            tm[(nx, ny)].append((d, K))
        for (x, y) in list(tm):
            if len(tm[(x, y)]) >= 2:
                ans += sum(map(lambda x: x[1], tm[(x, y)]))
                tm.pop((x, y))
        m = tm
    print(f'#{test_case} {ans}')
