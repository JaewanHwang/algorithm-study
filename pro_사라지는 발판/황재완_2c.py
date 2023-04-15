dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0
N, M = 0, 0


def go_A(x, y, ox, oy, m):
    if m[x][y] == 0:
        return False, 0
    win_cnt, lose_cnt = float('inf'), 0
    can_win, can_go = False, False
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 1:
            can_go = True
            m = [row[:] for row in m]
            m[x][y] = 0
            res, cnt = go_B(ox, oy, nx, ny, m)
            if res:
                lose_cnt = max(lose_cnt, cnt)
            else:
                can_win = True
                win_cnt = min(win_cnt, cnt)
    if not can_go:
        return False, 0
    if can_win:
        return True, 1 + win_cnt
    else:
        return False, 1 + lose_cnt


def go_B(x, y, ox, oy, m):
    if m[x][y] == 0:
        return False, 0
    win_cnt, lose_cnt = float('inf'), 0
    can_win, can_go = False, False
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and m[nx][ny] == 1:
            can_go = True
            m = [row[:] for row in m]
            m[x][y] = 0
            res, cnt = go_A(ox, oy, nx, ny, m)
            if res:
                lose_cnt = max(lose_cnt, cnt)
            else:
                can_win = True
                win_cnt = min(win_cnt, cnt)
    if not can_go:
        return False, 0
    if can_win:
        return True, 1 + win_cnt
    else:
        return False, 1 + lose_cnt


def solution(board, aloc, bloc):
    global N, M
    N, M = len(board), len(board[0])
    ax, ay = aloc
    bx, by = bloc
    res, ans = go_A(ax, ay, bx, by, board)
    return ans
