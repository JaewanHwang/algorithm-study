import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1),
block_map = {
    '|': {0: 0, 2: 2},
    '-': {1: 1, 3: 3},
    '+': {0: 0, 1: 1, 2: 2, 3: 3},
    '1': {3: 2, 0: 1},
    '2': {2: 1, 3: 0},
    '3': {2: 3, 1: 0},
    '4': {1: 2, 0: 3}
}
R, C = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]
blocks = []
for x in range(R):
    for y in range(C):
        if m[x][y] == 'M':
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < R and 0 <= ny < C and m[nx][ny] != '.':
                    sx, sy, sd = nx, ny, k
                    break
            m[x][y] = '.'
        elif m[x][y] == 'Z':
            ex, ey = x, y
            m[x][y] = '.'
        elif m[x][y] != '.':
            blocks.append((x, y))


def simulate():
    x, y, d = sx, sy, sd
    while 0 <= x < R and 0 <= y < C and m[x][y] != '.' and d in block_map[m[x][y]]:
        if (x, y) in remain:
            remain.remove((x, y))
        d = block_map[m[x][y]][d]
        nx, ny = x + dx[d], y + dy[d]
        x, y = nx, ny

    if remain or (x, y) != (ex, ey):
        return False
    else:
        return True


for x in range(R):
    for y in range(C):
        if m[x][y] != '.':
            continue
        for block in ('|', '-', '+', '1', '2', '3', '4'):
            remain = set(blocks)
            remain.add((x, y))
            m[x][y] = block
            if simulate():
                print(x + 1, y + 1, block)
                sys.exit(0)
            m[x][y] = '.'
