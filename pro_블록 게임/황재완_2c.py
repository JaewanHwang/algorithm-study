checker = [
    [(1, 0), (1, 1), (1, 2), (0, 1), (0, 2)],
    [(1, 0), (2, 0), (2, -1), (0, -1), (1, -1)],
    [(1, 0), (2, 0), (2, 1), (0, 1), (1, 1)],
    [(1, 0), (1, -1), (1, -2), (0, -1), (0, -2)],
    [(1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
]


def check(x, y, board):
    N = len(board)
    for k in range(5):
        removed = [(x, y)]
        ok = True
        for dx, dy in checker[k][:3]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != board[x][y]:
                ok = False
                break
            removed.append((nx, ny))
        if not ok:
            continue
        for dx, dy in checker[k][3:]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != 0:
                ok = False
                break
            for tx in range(nx):
                if board[tx][ny] != 0:
                    ok = False
                    break
            removed.append((nx, ny))
        if not ok:
            continue
        for rx, ry in removed:
            board[rx][ry] = 0
        return True
    return False


def solution(board):
    N = len(board)
    ok = True
    ans = 0
    while ok:
        ok = False
        for x in range(N):
            for y in range(N):
                if board[x][y] == 0:
                    continue
                if check(x, y, board):
                    ans += 1
                    ok = True
    return ans
