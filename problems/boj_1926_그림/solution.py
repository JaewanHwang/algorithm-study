import sys
from collections import deque

sys.stdin = open('input.txt')

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0]


def bfs(x, y):
    size = 1
    q = deque([(x, y)])
    board[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                size += 1
                q.append((nx, ny))
                board[nx][ny] = 0

    ans[1] = max(ans[1], size)


for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            ans[0] += 1
            bfs(x, y)

print(*ans, sep='\n')
