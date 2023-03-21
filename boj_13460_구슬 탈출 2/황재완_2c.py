import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(input().rstrip()) for _ in range(N)]
d = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for x in range(N):
    for y in range(M):
        if m[x][y] == 'B':
            m[x][y] = '.'
            bx, by = x, y
        elif m[x][y] == 'R':
            m[x][y] = '.'
            ax, ay = x, y

d[ax][ay][bx][by] = 0
q = deque([(ax, ay, bx, by)])


def go(x, y, k):
    moved = 0
    while True:
        if m[x][y] == 'O':
            break
        nx, ny = x + dx[k], y + dy[k]
        if m[nx][ny] == '#':
            break
        x, y = nx, ny
        moved += 1
    return x, y, moved


ans = -1
while q:
    ax, ay, bx, by = q.popleft()
    if m[bx][by] == 'O':
        continue
    elif m[ax][ay] == 'O':
        ans = d[ax][ay][bx][by]
        break
    if d[ax][ay][bx][by] == 10:
        continue
    for k in range(4):
        nax, nay, moved_a = go(ax, ay, k)
        nbx, nby, moved_b = go(bx, by, k)
        if (nax, nay) == (nbx, nby) and m[nax][nay] == '.':
            if moved_a > moved_b:
                nax, nay = nax - dx[k], nay - dy[k]
            else:
                nbx, nby = nbx - dx[k], nby - dy[k]
        if d[nax][nay][nbx][nby] == -1:
            q.append((nax, nay, nbx, nby))
            d[nax][nay][nbx][nby] = d[ax][ay][bx][by] + 1

print(ans)
