import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
m = [list(input().rstrip()) for _ in range(5)]
ans = 0


def go(comb):
    # comb = set(map(lambda x: (x // 5, x % 5), comb))
    q = deque()
    q.append(comb.pop())
    cnt = 0
    while q:
        index = q.popleft()
        x, y = index // 5, index % 5
        cnt += 1 if m[x][y] == 'Y' else 0
        if cnt > 3:
            return 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            nindex = nx * 5 + ny
            if 0 <= nx < 5 and 0 <= ny < 5 and nindex in comb:
                comb.remove(nindex)
                q.append(nindex)
    if not comb:
        return 1
    else:
        return 0


for comb in combinations(range(25), r=7):
    ans += go(set(comb))

print(ans)
