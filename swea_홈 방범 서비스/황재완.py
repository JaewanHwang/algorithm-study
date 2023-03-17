import sys

sys.stdin = open("input.txt", "r")

from collections import deque

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(x, y, k):
    coverage = 1 if m[x][y] == 1 else 0
    visit_cnt = 1
    q = deque([(x, y)])
    d = [[-1] * N for _ in range(N)]
    d[x][y] = 1
    while q:
        x, y = q.popleft()
        if d[x][y] == k:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
                visit_cnt += 1
                if m[nx][ny] == 1:
                    coverage += 1
    return coverage, visit_cnt


def simulate():
    max_coverage = 0
    for x in range(N):
        for y in range(N):
            k = 1
            while True:
                coverage, visit_cnt = go(x, y, k)
                if M * coverage - (k * k + (k - 1) * (k - 1)) >= 0:
                    max_coverage = max(max_coverage, coverage)
                if visit_cnt == N * N:
                    break
                k += 1
    return max_coverage


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    ans = simulate()
    print(f'#{test_case} {ans}')
