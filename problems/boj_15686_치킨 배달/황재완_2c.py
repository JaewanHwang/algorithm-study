import sys
from itertools import combinations

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for x in range(N):
    for y in range(N):
        if m[x][y] == 1:
            houses.append((x, y))
        elif m[x][y] == 2:
            chickens.append((x, y))


def simulate(case):
    res = 0
    for hx, hy in houses:
        res += min(abs(cx - hx) + abs(cy - hy) for cx, cy in case)
    return res


ans = float('inf')
for case in combinations(chickens, r=M):
    ans = min(ans, simulate(case))
print(ans)
