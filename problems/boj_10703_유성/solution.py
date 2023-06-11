import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

R, S = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]
min_diff = R
for y in range(S):
    last_star = first_land = -1
    for x in range(R):
        if m[x][y] == 'X':
            last_star = x
        elif m[x][y] == '#':
            if first_land == -1:
                first_land = x
    if last_star != -1:
        min_diff = min(min_diff, first_land - last_star - 1)

for y in range(S):
    for x in range(R - 1, -1, -1):
        if m[x][y] == 'X':
            m[x + min_diff][y] = m[x][y]
            m[x][y] = '.'
for row in m:
    print(''.join(row))
