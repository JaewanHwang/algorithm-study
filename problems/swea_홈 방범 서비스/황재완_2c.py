import sys

sys.stdin = open("input.txt", "r")


def go(x, y, K):
    cnt = 0
    for hx, hy in houses:
        if abs(hx - x) + abs(hy - y) < K:
            cnt += 1
    return cnt


def simulate():
    ans = 0
    for x in range(N):
        for y in range(N):
            for K in range(1, N + 2):
                cnt = go(x, y, K)
                if cnt * M - cost[K] >= 0:
                    ans = max(ans, cnt)
                    if ans == len(houses):
                        return ans
    return ans


T = int(input())
cost = [0] * 22
for k in range(1, 22):
    cost[k] = k * k + (k - 1) * (k - 1)
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    for x in range(N):
        for y in range(N):
            if m[x][y] == 1:
                houses.append((x, y))
    print(f'#{test_case} {simulate()}')
