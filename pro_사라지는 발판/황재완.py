dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
R, C = 0, 0


def go_A(x, y, ox, oy, board):
    board = [row[:] for row in board]
    if board[x][y] == 0:
        return 'L', 0
    tot = [-float('inf'), float('inf')]
    res = {'L': 0, 'W': 0}
    loop = 0
    board[x][y] = 0

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 1:
            status, cnt = go_B(ox, oy, nx, ny, board)
            if status == 'L':
                tot[1] = min(tot[1], cnt + 1)
            elif status == 'W':
                tot[0] = max(tot[0], cnt + 1)
            res[status] += 1
            loop += 1
    if loop == 0:
        return 'L', 0
    if res['W'] == loop:
        return 'L', tot[0]
    else:
        return 'W', tot[1]


def go_B(x, y, ox, oy, board):
    board = [row[:] for row in board]
    if board[x][y] == 0:
        return 'L', 0
    tot = [-float('inf'), float('inf')]
    res = {'L': 0, 'W': 0}
    loop = 0
    board[x][y] = 0

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 1:
            status, cnt = go_A(ox, oy, nx, ny, board)
            if status == 'L':
                tot[1] = min(tot[1], cnt + 1)
            elif status == 'W':
                tot[0] = max(tot[0], cnt + 1)
            res[status] += 1
            loop += 1
    if loop == 0:
        return 'L', 0
    if res['W'] == loop:
        return 'L', tot[0]
    else:
        return 'W', tot[1]


def solution(board, aloc, bloc):
    global R, C
    R, C = len(board), len(board[0])
    ax, ay = aloc
    bx, by = bloc
    win_or_lose, ans = go_A(ax, ay, bx, by, board)
    return ans


print(solution([[1]], [0, 0], [0, 0]))
