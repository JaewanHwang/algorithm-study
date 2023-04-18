import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
T = int(input())
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs():
    q = deque([(sx, sy, 0)])
    d = set()
    d.add((sx, sy))
    while q:
        x, y, dist = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (nx, ny) in d:
                continue
            if 0 <= nx < h and 0 <= ny < w:
                if m[nx][ny] != '#' and m[nx][ny] > dist + 1:
                    q.append((nx, ny, dist + 1))
                    d.add((nx, ny))
            else:
                return dist + 1
    return 'IMPOSSIBLE'


ans = []
for _ in range(T):
    w, h = map(int, input().split())
    m = [list(input().rstrip()) for _ in range(h)]
    q = deque()
    for x in range(h):
        for y in range(w):
            if m[x][y] == '*':
                q.append((x, y))
                m[x][y] = 0
            elif m[x][y] == '@':
                sx, sy = x, y
                m[x][y] = float('inf')
            elif m[x][y] == '.':
                m[x][y] = float('inf')

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and m[nx][ny] == float('inf'):
                m[nx][ny] = m[x][y] + 1
                q.append((nx, ny))
    ans.append(bfs())

print(*ans, sep='\n')
