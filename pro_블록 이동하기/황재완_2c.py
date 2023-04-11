from collections import deque

dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)


def solution(board):
    N = len(board)
    d = [[[[-1] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    q = deque([(0, 0, 0, 1, 2), (0, 1, 0, 0, 6)])
    d[0][0][0][1] = d[0][1][0][0] = 0
    while q:
        x, y, ox, oy, k = q.popleft()
        if (x, y) == (N - 1, N - 1) or (ox, oy) == (N - 1, N - 1):
            return d[x][y][ox][oy]
        # 1. 상하 좌우 이동
        for dir in range(0, 8, 2):
            nx, ny, nox, noy = x + dx[dir], y + dy[dir], ox + dx[dir], oy + dy[dir]
            if 0 <= nx < N and 0 <= ny < N and 0 <= nox < N and 0 <= noy < N and board[nx][ny] == 0 and board[nox][
                noy] == 0 and d[nx][ny][nox][noy] == -1:
                d[nx][ny][nox][noy] = d[nox][noy][nx][ny] = d[x][y][ox][oy] + 1
                q.extend([(nx, ny, nox, noy, k), (nox, noy, nx, ny, (k + 4) % 8)])
        # 2. 회전 이동
        # 2-1. 90도 시계방향
        for di in (1, -1):
            ok = True
            nk = k
            for i in range(1, 3):
                nk = (k + i * di) % 8
                nx, ny = x + dx[nk], y + dy[nk]
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:
                    ok = False
                    break
            if ok and d[x][y][nx][ny] == -1:
                d[x][y][nx][ny] = d[nx][ny][x][y] = d[x][y][ox][oy] + 1
                q.extend([(x, y, nx, ny, nk), (nx, ny, x, y, (nk + 4) % 8)])


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
