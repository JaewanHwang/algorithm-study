def solution(board, skill):
    N, M = len(board), len(board[0])
    acc = [[0] * (M + 1) for _ in range(N + 1)]
    for type, x1, y1, x2, y2, degree in skill:
        if type == 1:
            degree = -degree
        acc[x1][y1] += degree
        acc[x1][y2 + 1] -= degree
        acc[x2 + 1][y2 + 1] += degree
        acc[x2 + 1][y1] -= degree
    for x in range(N):
        for y in range(1, M):
            acc[x][y] += acc[x][y - 1]
    for y in range(M):
        for x in range(1, N):
            acc[x][y] += acc[x - 1][y]
    ans = 0
    for x in range(N):
        for y in range(M):
            if acc[x][y] + board[x][y] > 0:
                ans += 1
    return ans
