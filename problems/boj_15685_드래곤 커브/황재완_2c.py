import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)
m = [[False] * 101 for _ in range(101)]
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    nx, ny = x + dx[d], y + dy[d]
    m[x][y] = m[nx][ny] = True
    dragon_curve = [d]
    x, y = nx, ny
    for _ in range(g):
        for i in range(len(dragon_curve) - 1, -1, -1):
            nd = (dragon_curve[i] + 1) % 4
            dragon_curve.append(nd)
            nx, ny = x + dx[nd], y + dy[nd]
            m[nx][ny] = True
            x, y = nx, ny
ans = 0
for x in range(100):
    for y in range(100):
        if m[x][y] and m[x][y + 1] and m[x + 1][y + 1] and m[x + 1][y]:
            ans += 1
print(ans)
