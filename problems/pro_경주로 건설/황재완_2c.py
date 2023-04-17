from collections import deque

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)


def solution(board):
    N = len(board)
    d = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
    q = deque()
    for k in range(4):
        d[0][0][k] = 0
        q.append((0, 0, k))
    while q:
        x, y, dir = q.popleft()
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and (
                d[nx][ny][dir] == -1 or d[nx][ny][dir] > d[x][y][dir] + 100):
            q.append((nx, ny, dir))
            d[nx][ny][dir] = d[x][y][dir] + 100
        for k in (1, -1):
            ndir = (dir + k) % 4
            nx, ny = x + dx[ndir], y + dy[ndir]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and (
                    d[nx][ny][ndir] == -1 or d[nx][ny][ndir] > d[x][y][dir] + 600):
                q.append((nx, ny, ndir))
                d[nx][ny][ndir] = d[x][y][dir] + 600
    ans = -1
    for dist in d[N - 1][N - 1]:
        if ans == -1 or -1 < dist < ans:
            ans = dist
    return ans
