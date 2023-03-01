from collections import deque

dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
opposite_dir = {0: 4, 4: 0, 2: 6, 6: 2}


def solution(board):
    N = len(board)
    d = [[[-1] * 8 for _ in range(N)] for _ in range(N)]
    d[0][0][2], d[0][1][6] = 0, 0
    q = deque([(0, 0, 2), (0, 1, 6)])
    while q:
        x, y, ds = q.popleft()
        ox, oy, ods = x + dx[ds], y + dy[ds], opposite_dir[ds]
        # 상하좌우
        for i in range(0, 8, 2):
            nx, ny = x + dx[i], y + dy[i]
            nox, noy = ox + dx[i], oy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and 0 <= nox < N and 0 <= noy < N and board[nx][ny] == 0 and board[nox][
                noy] == 0:
                if d[nx][ny][ds] == -1:
                    d[nx][ny][ds] = d[x][y][ds] + 1
                    q.append((nx, ny, ds))

        for di in (-1, 1):
            nds = (ds + di * 2) % 8
            dnx, dny = x + dx[(ds + di * 1) % 8], y + dy[(ds + di * 1) % 8]
            nx, ny = x + dx[nds], y + dy[nds]
            if 0 <= dnx < N and 0 <= dny < N and board[dnx][dny] == 0 and 0 <= nx < N and 0 <= ny < N and board[nx][
                ny] == 0:
                if d[x][y][nds] == -1:
                    d[x][y][nds] = d[x][y][ds] + 1
                    q.append((x, y, nds))
                if d[nx][ny][opposite_dir[nds]] == -1:
                    d[nx][ny][opposite_dir[nds]] = d[x][y][ds] + 1
                    q.append((nx, ny, opposite_dir[nds]))

    ans = min(filter(lambda x: x >= 0, d[N - 1][N - 1]))
    return ans


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
