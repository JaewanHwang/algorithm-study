from collections import defaultdict, deque

N = 4
cards = defaultdict(list)
ans = float('inf')
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(x, y, cnt, rest, m):
    global ans
    if cnt >= ans:
        return
    if not rest:
        ans = cnt
        return
    for card in rest:
        for i, (cx, cy) in enumerate(cards[card]):
            nm = [row[:] for row in m]
            n_rest = set(rest)
            n_rest.remove(card)
            res = bfs(x, y, cx, cy, nm) + 1
            nm[cx][cy] = 0
            tx, ty = cards[card][1 - i]
            res += bfs(cx, cy, tx, ty, nm) + 1
            nm[tx][ty] = 0
            go(tx, ty, cnt + res, n_rest, nm)


def bfs(x, y, cx, cy, m):
    q = deque([(x, y)])
    d = [[-1] * N for _ in range(N)]
    d[x][y] = 0
    while q:
        x, y = q.popleft()
        if (x, y) == (cx, cy):
            return d[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
            while 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0:
                nx, ny = nx + dx[k], ny + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                nx, ny = nx - dx[k], ny - dy[k]
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))


def solution(board, r, c):
    rest = set()
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                cards[board[x][y]].append((x, y))
                rest.add(board[x][y])
    go(r, c, 0, rest, board)
    return ans
