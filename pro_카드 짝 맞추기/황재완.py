from collections import deque

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def solution(board, r, c):
    cards = []
    for x in range(4):
        for y in range(4):
            if board[x][y] > 0:
                tmp = len(cards)
                cards.append(board[x][y] - 1)
                board[x][y] = tmp
            else:
                board[x][y] = -1
    flag = 1
    for card in cards:
        flag |= 1 << card
    N = len(cards)
    d = [[[[-1] * (2 ** 6) for _ in range(N + 1)] for _ in range(4)] for _ in range(4)]
    d[r][c][N][flag] = 0
    q = deque([(r, c, N, flag)])
    while q:
        x, y, top, flag = q.popleft()
        if flag == 0:
            return d[x][y][top][flag]
        # 1. enter를 친다.
        if 0 <= board[x][y] < N and flag & 1 << cards[board[x][y]] and top != board[x][y]:
            if 0 <= top < N:
                new_flag = flag ^ 1 << cards[top] if cards[board[x][y]] == cards[top] else flag
                new_top = N
            elif top == N:
                new_top = board[x][y]
                new_flag = flag
            if d[x][y][new_top][new_flag] == -1:
                d[x][y][new_top][new_flag] = d[x][y][top][flag] + 1
                q.append((x, y, new_top, new_flag))

        # 2. 상하좌우로 이동한다.
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and d[nx][ny][top][flag] == -1:
                d[nx][ny][top][flag] = d[x][y][top][flag] + 1
                q.append((nx, ny, top, flag))
            nx, ny = x, y
            while 0 <= nx + dx[i] < 4 and 0 <= ny + dy[i] < 4:
                nx, ny = nx + dx[i], ny + dy[i]
                if 0 <= board[nx][ny] < N and flag & 1 << cards[board[nx][ny]]:
                    break
            if d[nx][ny][top][flag] == -1:
                d[nx][ny][top][flag] = d[x][y][top][flag] + 1
                q.append((nx, ny, top, flag))


print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
