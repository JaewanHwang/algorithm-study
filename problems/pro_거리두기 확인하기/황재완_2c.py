from collections import deque

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y, m):
    d = [[-1] * 5 for _ in range(5)]
    q = deque([(x, y)])
    d[x][y] = 0
    while q:
        x, y = q.popleft()
        if d[x][y] == 2:
            continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and d[nx][ny] == -1 and m[nx][ny] != 'X':
                if m[nx][ny] == 'P':
                    return False
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
    return True


def solution(places):
    ans = [1] * 5
    for i, m in enumerate(places):
        m = [list(row) for row in m]
        for x in range(5):
            for y in range(5):
                if m[x][y] != 'P':
                    continue
                if not bfs(x, y, m):
                    ans[i] = 0
                    break
    return ans
