patterns = [[(1, 0), (1, 1), (1, 2), (0, 1), (0, 2)],
            [(1, 0), (2, 0), (2, -1), (0, -1), (1, -1)],
            [(1, 0), (2, 0), (2, 1), (0, 1), (1, 1)],
            [(1, 0), (1, -1), (1, -2), (0, -1), (0, -2)],
            [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]]


def ok(board, x, y, pi):
    for dx, dy in patterns[pi][3:]:
        nx, ny = x + dx, y + dy
        for r in range(nx, -1, -1):
            if board[r][ny] != 0:
                return False
    return True


def solution(board):
    N = len(board)
    ans = 0
    candidate = set()
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                for pi, pattern in enumerate(patterns):
                    failed = False
                    for dx, dy in pattern[:3]:
                        if not (0 <= x + dx < N and 0 <= y + dy < N and board[x][y] == board[x + dx][y + dy]):
                            failed = True
                            break
                    if not failed:
                        candidate.add((x, y, pi))
                        break
    while True:
        remove_candidate = set()
        for x, y, pi in candidate:
            if ok(board, x, y, pi):
                board[x][y] = 0
                for dx, dy in patterns[pi][:3]:
                    board[x + dx][y + dy] = 0
                ans += 1
                remove_candidate.add((x, y, pi))

        if not remove_candidate:
            break

        for remove in remove_candidate:
            candidate.remove(remove)

    return ans
