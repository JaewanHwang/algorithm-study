import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def check():
    for x in range(3):
        if m[x][0] == m[x][1] == m[x][2] != '.':
            return True
    for y in range(3):
        if m[0][y] == m[1][y] == m[2][y] != '.':
            return True
    if m[0][0] == m[1][1] == m[2][2] != '.':
        return True
    if m[2][0] == m[1][1] == m[0][2] != '.':
        return True
    return False


def go(i, turn):
    if i == TOTAL:
        if TOTAL == 9 or check():
            return True
        else:
            return False

    if check():
        return False

    for j in range(len(picks[turn])):
        if selected[turn][j]:
            continue
        x, y = picks[turn][j]
        selected[turn][j] = True
        m[x][y] = turn
        if go(i + 1, 1 - turn):
            return True
        selected[turn][j] = False
        m[x][y] = '.'
    return False


while True:
    line = input().rstrip()
    if line == 'end':
        break
    picks = [[] for _ in range(2)]
    for x in range(3):
        for y in range(3):
            if line[x * 3 + y] == 'X':
                picks[0].append((x, y))
            elif line[x * 3 + y] == 'O':
                picks[1].append((x, y))
    m = [['.'] * 3 for _ in range(3)]
    selected = [[False] * len(picks[i]) for i in range(2)]
    TOTAL = len(picks[0]) + len(picks[1])
    if go(0, 0):
        print('valid')
    else:
        print('invalid')
