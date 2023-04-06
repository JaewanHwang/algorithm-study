import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")

T = int(input())
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    m = dict()
    arr = [[] for _ in range(K + 2)]
    dead = [0] * (K + 2)
    ans = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] == 0:
                continue
            m[(x, y)] = board[x][y]
            arr[board[x][y] + 1].append((x, y, board[x][y]))
            dead[board[x][y] * 2] += 1
            ans += 1
    for k in range(1, K + 1):
        increment = defaultdict(int)
        for x, y, p in arr[k]:
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if (nx, ny) not in m:
                    increment[(nx, ny)] = max(increment[(nx, ny)], p)
        for (x, y), p in increment.items():
            m[(x, y)] = p
            arr[min(K + 1, k + p + 1)].append((x, y, p))
            dead[min(K + 1, k + p * 2)] += 1
        ans += len(increment) - dead[k]
    print(f'#{test_case} {ans}')
