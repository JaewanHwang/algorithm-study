import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

side_map = {
    'U': [('B', 2, -1, 1), ('R', -1, 0, 1), ('F', 0, -1, -1), ('L', -1, 2, -1)],
    'F': [('U', 2, -1, 1), ('R', 2, -1, 1), ('D', 0, -1, -1), ('L', 2, -1, 1)],
    'D': [('F', 2, -1, 1), ('R', -1, 2, -1), ('B', 0, -1, -1), ('L', -1, 0, 1)],
    'L': [('U', -1, 0, 1), ('F', -1, 0, 1), ('D', -1, 0, 1), ('B', -1, 0, 1)],
    'R': [('U', -1, 2, -1), ('B', -1, 2, -1), ('D', -1, 2, -1), ('F', -1, 2, -1)],
    'B': [('U', 0, -1, -1), ('L', 0, -1, -1), ('D', 2, -1, 1), ('R', 0, -1, -1)]
}


def rotate_phase(phase, dir):
    tmp = [[0] * 3 for _ in range(3)]
    if dir == '+':
        for x in range(3):
            for y in range(3):
                tmp[x][y] = cube[phase][2 - y][x]
    else:
        for x in range(3):
            for y in range(3):
                tmp[x][y] = cube[phase][y][2 - x]
    cube[phase] = tmp


def rotate_sides(phase, dir):
    q = deque()
    for p, x, y, d in side_map[phase]:
        loop = range(0, 3, 1) if d == 1 else range(2, -1, -1)
        if x != -1:
            for y in loop:
                q.append(cube[p][x][y])
        else:
            for x in loop:
                q.append(cube[p][x][y])
    q.rotate(3 * (1 if dir == '+' else -1))
    for p, x, y, d in side_map[phase]:
        loop = range(0, 3, 1) if d == 1 else range(2, -1, -1)
        if x != -1:
            for y in loop:
                cube[p][x][y] = q.popleft()
        else:
            for x in loop:
                cube[p][x][y] = q.popleft()


TC = int(input())
for _ in range(TC):
    n = int(input())
    operations = input().split()
    cube = {
        'U': [['w'] * 3 for _ in range(3)],
        'F': [['r'] * 3 for _ in range(3)],
        'D': [['y'] * 3 for _ in range(3)],
        'L': [['g'] * 3 for _ in range(3)],
        'R': [['b'] * 3 for _ in range(3)],
        'B': [['o'] * 3 for _ in range(3)],
    }
    for phase, dir in operations:
        rotate_phase(phase, dir)
        rotate_sides(phase, dir)
    print(*(''.join(row) for row in cube['U']), sep='\n')
