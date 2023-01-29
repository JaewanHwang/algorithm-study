def solution(m, n, board):
    answer = 0
    board = [list(row) for row in  board]
    while True:
        removed = set()
        for x in range(m - 1):
            for y in range(n - 1):
                if board[x][y] == board[x][y + 1] == board[x + 1][y + 1] == board[x + 1][y] != 0:
                    removed.add((x, y))
                    removed.add((x, y + 1))
                    removed.add((x + 1, y + 1))
                    removed.add((x + 1, y))
        if not removed:
            break
        answer += len(removed)
        for x, y in removed:
            board[x][y] = 0
        for y in range(n):
            cx = m - 1
            for x in range(m - 1, -1, -1):
                if board[x][y] != 0:
                    tmp = board[x][y]
                    board[x][y] = 0
                    board[cx][y] = tmp
                    cx -= 1

    return answer