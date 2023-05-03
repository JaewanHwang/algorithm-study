import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (0, 1, 1, 1, 0, 0, 0, -1, -1, -1), (0, -1, 0, 1, -1, 0, 1, -1, 0, 1)
R, C = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]
ops = list(map(int, input().rstrip()))

arduino = set()
for x in range(R):
    for y in range(C):
        if m[x][y] == 'I':
            player = x, y
            m[x][y] = '.'
        elif m[x][y] == 'R':
            arduino.add((x, y))
            m[x][y] = '.'

for t, d in enumerate(ops, start=1):
    x, y = player
    nx, ny = x + dx[d], y + dy[d]
    if (nx, ny) in arduino:
        print(f'kraj {t}')
        sys.exit(0)
    player = (nx, ny)
    new_arduino = set()
    removed = set()
    for ax, ay in arduino:
        candi = []
        for k in range(1, 10):
            if k == 5:
                continue
            nax, nay = ax + dx[k], ay + dy[k]
            if 0 <= nax < R and 0 <= nay < C:
                candi.append((abs(nax - player[0]) + abs(nay - player[1]), nax, nay))
        _, nax, nay = min(candi)
        if (nax, nay) in new_arduino:
            removed.add((nax, nay))
        new_arduino.add((nax, nay))
    if player in new_arduino:
        print(f'kraj {t}')
        sys.exit(0)
    arduino = new_arduino - removed

m[player[0]][player[1]] = 'I'
for x, y in arduino:
    m[x][y] = 'R'
for row in m:
    print(''.join(row))
