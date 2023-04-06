import sys
from collections import deque

sys.stdin = open("input.txt", "r")


def simulate(case):
    ready_qs = [[] for _ in range(2)]
    for i, (px, py) in enumerate(people):
        si = 1 if case & 1 << i else 0
        sx, sy, _ = staircases[si]
        ready_qs[si].append(abs(px - sx) + abs(py - sy) + 1)

    res = 0
    for i, ready_q in enumerate(ready_qs):
        ready_q.sort(reverse=True)
        staircase_q = deque()
        cur = 0
        k = staircases[i][2]
        while ready_q or staircase_q:
            if staircase_q:
                cur = staircase_q[0]
                while staircase_q and cur == staircase_q[0]:
                    res = max(res, staircase_q.popleft())
            for _ in range(3 - len(staircase_q)):
                if ready_q:
                    staircase_q.append(max(cur, ready_q.pop()) + k)
    return res


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    staircases = []
    people = []
    for x in range(N):
        for y in range(N):
            if m[x][y] == 1:
                people.append((x, y))
            elif 2 <= m[x][y] <= 10:
                staircases.append((x, y, m[x][y]))
    ans = float('inf')
    for case in range(2 ** len(people)):
        ans = min(ans, simulate(case))
    print(f'#{test_case} {ans}')
