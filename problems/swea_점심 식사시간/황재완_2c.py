import sys
from collections import deque

sys.stdin = open("input.txt", "r")


def calculate(selected):
    ready_q = [[], []]
    for pi, si in enumerate(selected):
        px, py = people[pi]
        sx, sy = staircase[si]
        ready_q[si].append(abs(px - sx) + abs(py - sy) + 1)
    res = 0
    for si in range(2):
        q = deque(sorted(ready_q[si]))
        staircase_q = deque()
        sl = m[staircase[si][0]][staircase[si][1]]
        cur = 0
        while q or staircase_q:
            while q and len(staircase_q) < 3:
                cur = max(cur, q.popleft())
                staircase_q.append(cur + sl)
            if len(staircase_q) > 0:
                cur = staircase_q[0]
                while staircase_q and staircase_q[0] == cur:
                    staircase_q.popleft()
            if cur >= ans:
                return cur
        res = max(res, cur)
    return res


def go(i, selected):
    global ans
    if i == len(people):
        ans = min(ans, calculate(selected))
        return
    selected[i] = 1
    go(i + 1, selected)
    selected[i] = 0
    go(i + 1, selected)


def simulate():
    for x in range(N):
        for y in range(N):
            if m[x][y] == 1:
                people.append((x, y))
            elif 10 >= m[x][y] >= 2:
                staircase.append((x, y))
    selected = [0] * len(people)
    return go(0, selected)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    people = []
    staircase = []
    ans = float('inf')
    simulate()
    print(f'#{test_case} {ans}')
