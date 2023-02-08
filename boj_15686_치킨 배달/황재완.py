import sys
from itertools import combinations

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
chickens = []
houses = []
for x in range(N):
    for y in range(N):
        if m[x][y] == 2:
            chickens.append((x, y))
        elif m[x][y] == 1:
            houses.append((x, y))

ans = float('inf')
for case in combinations(chickens, r=M):
    res = 0
    for hx, hy in houses:
        res += min(map(lambda x: abs(hx - x[0]) + abs(hy - x[1]), case))
    ans = min(ans, res)

print(ans)
