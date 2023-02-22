from collections import deque

dx, dy = (-1, 1, 0, 0, -1, -1, 1, 1), (0, 0, -1, 1, -1, 1, 1, -1)


def solution(rectangle, characterX, characterY, itemX, itemY):
    m = [[0] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        for x in range(2 * x1, 2 * x2 + 1):
            for y in range(2 * y1, 2 * y2 + 1):
                m[x][y] = 1

    q = deque([(0, 0)])
    m[0][0] = -2
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx <= 101 and 0 <= ny <= 101 and m[nx][ny] >= 0:
                if m[nx][ny] == 1:
                    m[nx][ny] = -1
                elif m[nx][ny] == 0:
                    m[nx][ny] = -2
                    q.append((nx, ny))

    q = deque([(2 * characterX, 2 * characterY)])
    m[2 * characterX][2 * characterY] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx <= 101 and 0 <= ny <= 101 and m[nx][ny] == -1:
                q.append((nx, ny))
                m[nx][ny] = m[x][y] + 1
    ans = m[2 * itemX][2 * itemY] // 2
    return ans
