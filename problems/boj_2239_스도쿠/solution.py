import sys
from collections import Counter

sys.stdin = open('input.txt')
input = sys.stdin.readline

m = [list(map(int, input().rstrip())) for _ in range(9)]


def go(i):
    if i == 81:
        return True
    x, y = i // 9, i % 9
    if m[x][y] != 0:
        if go(i + 1):
            return True
        return False
    for num in range(1, 10):
        if cnt_row[x][num] == 0 and cnt_col[y][num] == 0 and cnt_box[x // 3][y // 3][num] == 0:
            cnt_row[x][num] += 1
            cnt_col[y][num] += 1
            cnt_box[x // 3][y // 3][num] += 1
            m[x][y] = num
            if go(i + 1):
                return True
            cnt_row[x][num] -= 1
            cnt_col[y][num] -= 1
            cnt_box[x // 3][y // 3][num] -= 1
            m[x][y] = 0
    return False


cnt_row = []
cnt_col = []
cnt_box = [[Counter() for _ in range(3)] for _ in range(3)]
for x in range(9):
    cnt_row.append(Counter(m[x]))
tm = list(zip(*m))
for x in range(9):
    cnt_col.append(Counter(tm[x]))
for sx in range(0, 9, 3):
    for sy in range(0, 9, 3):
        for x in range(sx, sx + 3):
            for y in range(sy, sy + 3):
                cnt_box[x // 3][y // 3][m[x][y]] += 1
go(0)
for row in m:
    print(''.join(map(str, row)))
