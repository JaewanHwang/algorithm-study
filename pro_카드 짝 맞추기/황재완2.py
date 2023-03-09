from collections import deque, defaultdict

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(sx, sy, ex, ey):
    d = [[-1] * 4 for _ in range(4)]
    q = deque([(sx, sy)])
    d[sx][sy] = 0
    while q:
        x, y = q.popleft()
        if (x, y) == (ex, ey):
            return d[ex][ey]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
            nx, ny = x, y
            while 0 <= nx + dx[i] < 4 and 0 <= ny + dy[i] < 4:
                nx, ny = nx + dx[i], ny + dy[i]
                if m[nx][ny] > 0:
                    break
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))


def go(i, x, y, tot):
    global ans, cnt
    if tot >= ans:
        return
    if i == N:
        ans = min(ans, tot)
        return
    for card in cards:
        if visited[card]:
            continue
        (x1, y1), (x2, y2) = cards[card]
        dist1 = bfs(x, y, x1, y1) + bfs(x1, y1, x2, y2)
        dist2 = bfs(x, y, x2, y2) + bfs(x2, y2, x1, y1)
        visited[card] = True
        m[x1][y1] = m[x2][y2] = 0
        go(i + 1, x2, y2, 2 + tot + dist1)
        go(i + 1, x1, y1, 2 + tot + dist2)
        m[x1][y1] = m[x2][y2] = card
        visited[card] = False


ans = float('inf')
m = None
cards = None
N = 0
visited = None


def solution(board, r, c):
    global m, cards, N, visited
    m = board
    cards = defaultdict(list)
    visited = dict()
    for x in range(4):
        for y in range(4):
            if m[x][y] > 0:
                cards[m[x][y]].append((x, y))
                visited[m[x][y]] = False
    N = len(cards)
    go(0, r, c, 0)
    return ans


print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
