import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)
m = [[False] * 101 for _ in range(101)]
N = int(input())
for _ in range(N):
    y, x, d, g = map(int, input().split())
    dirs = [d]
    nx, ny = x + dx[d], y + dy[d]
    m[x][y] = m[nx][ny] = True
    x, y = nx, ny
    for _ in range(g):
        for i in range(len(dirs) - 1, -1, -1):
            nd = (dirs[i] + 1) % 4
            dirs.append(nd)
            nx, ny = x + dx[nd], y + dy[nd]
            m[nx][ny] = True
            x, y = nx, ny

ans = 0
for x in range(100):
    for y in range(100):
        if m[x][y] and m[x + 1][y + 1] and m[x + 1][y] and m[x][y + 1]:
            ans += 1
print(ans)
