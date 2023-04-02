dx, dy = (0, 1, 1), (1, 0, 1)


def solution(m, n, board):
    board = [list(row) for row in board]
    ans = 0
    while True:
        removed = set()
        for x in range(m):
            for y in range(n):
                if not board[x][y]:
                    continue
                failed = False
                cur = {(x, y)}
                for k in range(3):
                    nx, ny = x + dx[k], y + dy[k]
                    if not (0 <= nx < m and 0 <= ny < n and board[x][y] == board[nx][ny]):
                        failed = True
                        break
                    cur.add((nx, ny))
                if not failed:
                    removed |= cur
        if not removed:
            break
        ans += len(removed)
        for x, y in removed:
            board[x][y] = 0
        for y in range(n):
            last_x = m - 1
            for x in range(m - 1, -1, -1):
                if not board[x][y]:
                    continue
                tmp = board[x][y]
                board[x][y] = 0
                board[last_x][y] = tmp
                last_x -= 1

    return ans
