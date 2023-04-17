import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

manipulate = {
    'U': ['B678', 'R036', 'F210', 'L852'],
    'D': ['F678', 'R852', 'B210', 'L036'],
    'F': ['U678', 'R678', 'D210', 'L678'],
    'B': ['U210', 'L210', 'D678', 'R210'],
    'L': ['U036', 'F036', 'D036', 'B036'],
    'R': ['U852', 'B852', 'D852', 'F852']
}
TC = int(input())


def simulate(p, d):
    q = deque()
    insert = []
    for line in manipulate[p]:
        for i in map(int, line[1:]):
            x, y = i // 3, i % 3
            insert.append((line[0], x, y))
            q.append(cube[line[0]][x][y])
    q.rotate(d * 3)
    for pi, x, y in insert:
        color = q.popleft()
        cube[pi][x][y] = color
    tplane = [[0] * 3 for _ in range(3)]
    for x in range(3):
        for y in range(3):
            if d == 1:
                tplane[x][y] = cube[p][2 - y][x]
            else:
                tplane[x][y] = cube[p][y][2 - x]
    cube[p] = tplane


for _ in range(TC):
    n = int(input())
    cube = {'U': [['w'] * 3 for _ in range(3)],
            'D': [['y'] * 3 for _ in range(3)],
            'F': [['r'] * 3 for _ in range(3)],
            'B': [['o'] * 3 for _ in range(3)],
            'L': [['g'] * 3 for _ in range(3)],
            'R': [['b'] * 3 for _ in range(3)]}
    for op in input().split():
        simulate(op[0], 1 if op[1] == '+' else -1)
    for row in cube['U']:
        print(''.join(row))
