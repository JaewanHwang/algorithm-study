import sys
from collections import deque

sys.stdin = open("input.txt", "r")

pipe_map = {
    1: {0, 1, 2, 3},
    2: {0, 2},
    3: {1, 3},
    4: {0, 1},
    5: {1, 2},
    6: {2, 3},
    7: {0, 3}
}
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    d = [[-1] * M for _ in range(N)]
    q = deque([(R, C)])
    d[R][C] = 1
    ans = 0
    while q:
        x, y, = q.popleft()
        ans += 1
        if d[x][y] == L:
            continue
        for k in pipe_map[m[x][y]]:
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and 1 <= m[nx][ny] <= 7 and (k + 2) % 4 in pipe_map[m[nx][ny]] and d[nx][
                ny] == -1:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1
    print(f'#{test_case} {ans}')
