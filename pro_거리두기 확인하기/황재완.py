from collections import deque

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(m, x, y):
    d = [[-1] * 5 for _ in range(5)]
    q = deque([(x, y)])
    d[x][y] = 0
    for _ in range(2):
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and d[nx][ny] == -1 and m[nx][ny] != 'X':
                    if m[nx][ny] == 'P':
                        return False
                    else:
                        q.append((nx, ny))
                        d[nx][ny] = d[x][y] + 1
    return True


def test(place):
    m = [list(row) for row in place]
    for x in range(5):
        for y in range(5):
            if m[x][y] == 'P':
                if not bfs(m, x, y):
                    return False
    return True


def solution(places):
    ans = []
    for place in places:
        if test(place):
            ans.append(1)
        else:
            ans.append(0)
    return ans