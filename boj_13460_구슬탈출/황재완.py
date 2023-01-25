import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
N, M = map(int, input().split())
m = []
d = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
rx, ry, bx, by = -1, -1, -1, -1
for x in range(N):
    row = list(input().rstrip())
    for y in range(M):
        if row[y] == 'R':
            row[y] = '.'
            rx, ry = x, y
        elif row[y] == 'B':
            row[y] = '.'
            bx, by = x, y
    m.append(row)

q = deque()
q.append((rx, ry, bx, by))
d[rx][ry][bx][by] = 0
ans = -1

while q:
    rx, ry, bx, by = q.popleft()
    if m[rx][ry] == 'O':
        ans = d[rx][ry][bx][by]
        break
    if d[rx][ry][bx][by] == 10:
        continue

    for i in range(4):
        nrx, nry, nbx, nby = rx, ry, bx, by
        rm, bm = 0, 0
        blue_in_hole = False

        while m[nbx + dx[i]][nby + dy[i]] != '#':
            nbx, nby = nbx + dx[i], nby + dy[i]
            if m[nbx][nby] == 'O':
                blue_in_hole = True
                break
            bm += 1

        if blue_in_hole:
            continue

        while m[nrx + dx[i]][nry + dy[i]] != '#':
            nrx, nry = nrx + dx[i], nry + dy[i]
            if m[nrx][nry] == 'O':
                break
            rm += 1

        if nrx == nbx and nry == nby:
            if rm > bm:
                nrx, nry = nrx - dx[i], nry - dy[i]
            elif rm < bm:
                nbx, nby = nbx - dx[i], nby - dy[i]

        if d[nrx][nry][nbx][nby] == -1:
            d[nrx][nry][nbx][nby] = d[rx][ry][bx][by] + 1
            q.append((nrx, nry, nbx, nby))

print(ans)
