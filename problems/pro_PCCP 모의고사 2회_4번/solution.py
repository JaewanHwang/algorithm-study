from collections import deque

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def solution(n, m, hole):
    d = [[[-1] * 2 for _ in range(n)] for _ in range(m)]
    d[m - 1][0][False] = 0
    q = deque([(m - 1, 0, False)])
    obstacle = [[False] * n for _ in range(m)]
    for a, b in hole:
        obstacle[m - b][a - 1] = True
    while q:
        x, y, jumped = q.popleft()
        if (x, y) == (0, n - 1):
            return d[x][y][jumped]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and not obstacle[nx][ny] and d[nx][ny][jumped] == -1:
                d[nx][ny][jumped] = d[x][y][jumped] + 1
                q.append((nx, ny, jumped))
        if not jumped:
            for k in range(4):
                nx, ny = x + 2 * dx[k], y + 2 * dy[k]
                if 0 <= nx < m and 0 <= ny < n and not obstacle[nx][ny] and d[nx][ny][False] == -1:
                    d[nx][ny][True] = d[x][y][False] + 1
                    q.append((nx, ny, True))

    return -1
