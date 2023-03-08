patterns = [[(1, 0), (1, 1), (1, 2), (0, 1), (0, 2)],
            [(1, 0), (2, 0), (2, -1), (0, -1), (1, -1)],
            [(1, 0), (2, 0), (2, 1), (0, 1), (1, 1)],
            [(1, 0), (1, -1), (1, -2), (0, -1), (0, -2)],
            [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]]


def solution(board):
    N = len(board)
    ans = 0
    candidate = set()
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                for pi, pattern in enumerate(patterns):
                    ok = True
                    for dx, dy in pattern[:3]:
                        if not (0 <= x + dx < N and 0 <= y + dy < N and board[x][y] == board[x + dx][y + dy]):
                            ok = False
                            break
                    if ok:
                        candidate.add((x, y, pi))
                        break
    while True:
        remove_candidate = set()
        for x, y, pi in candidate:
            remove_position = set([(x, y)])
            ok = True
            for dx, dy in patterns[pi][:3]:
                nx, ny = x + dx, y + dy
                remove_position.add((nx, ny))
                for r in range(nx, -1, -1):
                    if board[r][ny] != 0 and board[r][ny] != board[x][y]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                for dx, dy in patterns[pi][3:]:
                    nx, ny = x + dx, y + dy
                    if board[nx][ny] > 0:
                        ok = False
                        break
            if ok:
                for rx, ry in remove_position:
                    board[rx][ry] = 0
                ans += 1
                remove_candidate.add((x, y, pi))

        if not remove_candidate:
            break

        candidate -= remove_candidate

    return ans


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
