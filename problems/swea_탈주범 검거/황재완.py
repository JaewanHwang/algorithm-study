import sys
from collections import deque

sys.stdin = open("input.txt", "r")
dx, dy = (-1, 0, 0, 1), (0, -1, 1, 0)
tunnel_map = {
    1: {0, 1, 2, 3},
    2: {0, 3},
    3: {1, 2},
    4: {0, 2},
    5: {2, 3},
    6: {1, 3},
    7: {0, 1}
}


def simulate():
    q = deque([(R, C, m[R][C])])
    m[R][C] = -1
    for _ in range(L - 1):
        for _ in range(len(q)):
            x, y, tk = q.popleft()
            for d in tunnel_map[tk]:
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and m[nx][ny] > 0 and 3 - d in tunnel_map[m[nx][ny]]:
                    q.append((nx, ny, m[nx][ny]))
                    m[nx][ny] = -1
    res = 0
    for x in range(N):
        for y in range(M):
            if m[x][y] == -1:
                res += 1
    return res


T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    ans = simulate()
    print(f'#{test_case} {ans}')
