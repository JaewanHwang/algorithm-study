from collections import deque

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def go(ox, oy, x, y, n, table, dirs):
    table[x][y] = 0
    dirs.append((ox - x, oy - y))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < len(table) and 0 <= ny < len(table) and table[nx][ny] == n:
            go(ox, oy, nx, ny, n, table, dirs)


def go2(ox, oy, x, y, game_board, dirs):
    game_board[x][y] = 1
    dirs.append((ox - x, oy - y))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < len(game_board) and 0 <= ny < len(game_board) and game_board[nx][ny] == 0:
            go2(ox, oy, nx, ny, game_board, dirs)


def solution(game_board, table):
    N = len(table)
    ans = 0
    for x in range(N):
        for y in range(N):
            if table[x][y] == 1:
                table[x][y] = -1

    puzzles = [set()]
    puzzle_num = 1
    for x in range(N):
        for y in range(N):
            if table[x][y] == -1:
                puzzles.append(set())
                q = deque([(x, y)])
                table[x][y] = puzzle_num
                while q:
                    r, c = q.popleft()
                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]
                        if 0 <= nr < N and 0 <= nc < N and table[nr][nc] == -1:
                            table[nr][nc] = puzzle_num
                            q.append((nr, nc))
                puzzle_num += 1

    for _ in range(4):
        tmp_table = [row[:] for row in table]
        for x in range(N):
            for y in range(N):
                if tmp_table[x][y] != 0:
                    dirs = []
                    num = tmp_table[x][y]
                    go(x, y, x, y, num, tmp_table, dirs)
                    puzzles[num].add(tuple(dirs))

        tmp_table = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                tmp_table[x][y] = table[N - 1 - y][x]
        table = tmp_table
    for x in range(N):
        for y in range(N):
            if game_board[x][y] == 0:
                dirs = []
                go2(x, y, x, y, game_board, dirs)
                dirs = tuple(dirs)
                for i in range(len(puzzles)):
                    if dirs in puzzles[i]:
                        ans += len(dirs)
                        puzzles.pop(i)
                        break

    return ans


ans = solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
               [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
print(ans)
