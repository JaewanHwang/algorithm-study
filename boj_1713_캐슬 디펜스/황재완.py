import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt')

N, M, D = map(int, input().split())
original_m = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (0, -1, 0), (-1, 0, 1)


def simulate(case):
    m = [row[:] for row in original_m]
    res = 0

    for _ in range(N):
        removed = set()
        for y in case:
            d = [[-1] * M for _ in range(N)]
            q = deque([(N - 1, y)])
            d[N - 1][y] = 1
            while q:
                x, y = q.popleft()
                if d[x][y] <= D and m[x][y] == 1:
                    removed.add((x, y))
                    break
                if d[x][y] == D:
                    continue
                for k in range(3):
                    nx, ny = x + dx[k], y + dy[k]
                    if nx >= 0 and 0 <= ny < M and d[nx][ny] == -1:
                        d[nx][ny] = d[x][y] + 1
                        q.append((nx, ny))

        res += len(removed)
        for x, y in removed:
            m[x][y] = 0

        m = [[0] * M] + m[:-1]
    return res


ans = 0
for case in combinations(range(M), r=3):
    ans = max(ans, simulate(case))
print(ans)
