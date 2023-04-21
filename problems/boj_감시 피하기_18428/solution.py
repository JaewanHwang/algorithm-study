import sys
from itertools import combinations

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(case):
    case = set(case)
    for tx, ty in teachers:
        for k in range(4):
            x, y = tx, ty
            while 0 <= x < N and 0 <= y < N and (x, y) not in case:
                if m[x][y] == 'S':
                    return False
                x, y = x + dx[k], y + dy[k]
    return True


N = int(input())
m = [list(input().split()) for _ in range(N)]
students = []
teachers = []
blanks = []
for x in range(N):
    for y in range(N):
        if m[x][y] == 'S':
            students.append((x, y))
        elif m[x][y] == 'T':
            teachers.append((x, y))
        else:
            blanks.append((x, y))

for case in combinations(blanks, r=3):
    if go(case):
        print('YES')
        sys.exit(0)
print('NO')
