import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N = int(input())
A = [[0] * (N + 1) for _ in range(N + 1)]

for x in range(1, N + 1):
    A[x][1:N + 1] = list(map(int, input().split()))
ans = float('inf')


def simulate():
    m = [[0] * (N + 1) for _ in range(N + 1)]
    people_cnt = [0] * 6
    for i in range(d1 + 1):
        m[x + i][y - i] = 5
        m[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        m[x + i][y + i] = 5
        m[x + d1 + i][y - d1 + i] = 5
    bfs(0, 0, m)
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if m[r][c] == 5:
                continue
            if 1 <= r < x + d1 and 1 <= c <= y:
                m[r][c] = 1
            elif 1 <= r <= x + d2 and y < c <= N:
                m[r][c] = 2
            elif x + d1 <= r <= N and 1 <= c < y - d1 + d2:
                m[r][c] = 3
            else:
                m[r][c] = 4
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            people_cnt[m[r][c]] += A[r][c]

    res = max(people_cnt[1:]) - min(people_cnt[1:])
    return res


def bfs(x, y, m):
    q = deque([(x, y)])
    m[x][y] = -1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx <= N and 0 <= ny <= N and m[nx][ny] == 0:
                q.append((nx, ny))
                m[nx][ny] = -1
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if m[x][y] == 0:
                m[x][y] = 5


for d1 in range(1, N):
    for d2 in range(1, N):
        for x in range(1, N):
            for y in range(1, N):
                if 1 <= x < x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N:
                    ans = min(ans, simulate())
print(ans)
