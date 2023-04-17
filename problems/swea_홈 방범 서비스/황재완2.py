import sys

sys.stdin = open("input.txt", "r")


def go(x, y, k, houses):
    coverage = 0
    for hx, hy in houses:
        if abs(hx - x) + abs(hy - y) < k:
            coverage += 1

    return coverage


def simulate():
    max_coverage = 0
    houses = []
    for x in range(N):
        for y in range(N):
            if m[x][y] == 1:
                houses.append((x, y))
    for x in range(N):
        for y in range(N):
            for k in range(1, 2 * N):
                coverage = go(x, y, k, houses)
                if M * coverage - (k * k + (k - 1) * (k - 1)) >= 0:
                    max_coverage = max(max_coverage, coverage)
    return max_coverage


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    ans = simulate()
    print(f'#{test_case} {ans}')
