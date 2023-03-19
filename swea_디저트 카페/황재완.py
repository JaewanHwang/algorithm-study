import sys
from itertools import product

sys.stdin = open("sample_input.txt", "r")
dx, dy = (1, 1, -1, -1), (1, -1, -1, 1)


def go(x, y, l1, l2):
    path = [0] * l1 + [1] * l2 + [2] * l1 + [3] * l2
    eaten_desserts = set()
    for k in path:
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return -1
        if m[nx][ny] in eaten_desserts:
            return -1
        eaten_desserts.add(m[nx][ny])
        x, y = nx, ny
    return len(eaten_desserts)


def simulate():
    max_cnt = -1
    for x in range(N):
        for y in range(N):
            for lengths in product(range(1, N), repeat=2):
                max_cnt = max(max_cnt, go(x, y, *lengths))
    return max_cnt


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    ans = simulate()
    print(f'#{test_case} {ans}')
