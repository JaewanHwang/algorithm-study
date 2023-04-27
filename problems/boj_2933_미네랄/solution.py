import sys
from collections import deque, defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
R, C = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]
N = int(input())


def bfs(x, y):
    on_bottom = True if x == R - 1 else False
    group = defaultdict(list)
    group[y].append(x)
    checked[x][y] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and m[nx][ny] == 'x' and not checked[nx][ny]:
                checked[nx][ny] = True
                q.append((nx, ny))
                group[ny].append(nx)
                if nx == R - 1:
                    on_bottom = True
    if on_bottom:
        return False
    min_down = R
    for y in group:
        x = max(group[y])
        for h in range(x, R):
            if h + 1 < R and m[h + 1][y] == 'x':
                break
        min_down = min(min_down, h - x)
    for y in group:
        for x in group[y]:
            m[x][y] = '.'
    for y in group:
        for x in group[y]:
            m[x + min_down][y] = 'x'
    return True


for turn, x in enumerate(map(lambda x: R - int(x), input().split())):
    broken = False
    for y in range(C) if turn % 2 == 0 else range(C - 1, -1, -1):
        if m[x][y] == 'x':
            m[x][y] = '.'
            broken = True
            break
    if not broken:
        continue

    checked = [[False] * C for _ in range(R)]
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and m[nx][ny] == 'x' and not checked[nx][ny]:
            if bfs(nx, ny):
                break

for row in m:
    print(''.join(row))
