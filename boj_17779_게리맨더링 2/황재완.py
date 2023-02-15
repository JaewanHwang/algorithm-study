import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')


def go(x, y, d1, d2):
    m = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(d1 + 1):
        m[x + d2 + i][y + d2 - i] = m[x + i][y - i] = 5
    for i in range(d2 + 1):
        m[x + d1 + i][y - d1 + i] = m[x + i][y + i] = 5

    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if m[r][c] == 5:
                break
            m[r][c] = 1

    for r in range(1, x + d2 + 1):
        for c in range(N, y, -1):
            if m[r][c] == 5:
                break
            m[r][c] = 2

    for r in range(x + d1, N + 1):
        for c in range(1, y - d1 + d2):
            if m[r][c] == 5:
                break
            m[r][c] = 3

    for r in range(x + d2 + 1, N + 1):
        for c in range(N, y - d1 + d2 - 1, -1):
            if m[r][c] == 5:
                break
            m[r][c] = 4

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if m[r][c] == 0:
                m[r][c] = 5

    tot_cnt = [0] * 6
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if not visited[x][y] and m[x][y] != 0:
                q = deque([(x, y)])
                tot_cnt[m[x][y]] += A[x - 1][y - 1]
                visited[x][y] = True

                while q:
                    r, c = q.popleft()
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 1 <= nr <= N and 1 <= nc <= N and m[nr][nc] == m[r][c] and not visited[nr][nc]:
                            q.append((nr, nc))
                            tot_cnt[m[nr][nc]] += A[nr - 1][nc - 1]
                            visited[nr][nc] = True
    tot_cnt = tot_cnt[1:]
    return max(tot_cnt) - min(tot_cnt)


for sx in range(1, N):
    for sy in range(1, N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if 1 <= sx < sx + d1 + d2 <= N and 1 <= sy - d1 < sy < sy + d2 <= N:
                    ans = min(ans, go(sx, sy, d1, d2))

print(ans)
