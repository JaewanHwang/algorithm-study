def solution(board, skill):
    N, M = len(board), len(board[0])
    acc_arr = [[0] * M for _ in range(N)]
    for type, r1, c1, r2, c2, degree in skill:
        type = -1 if type == 1 else 1
        acc_arr[r1][c1] += degree * type
        if r2 + 1 < N:
            acc_arr[r2 + 1][c1] -= degree * type
        if c2 + 1 < M:
            acc_arr[r1][c2 + 1] -= degree * type
        if r2 + 1 < N and c2 + 1 < N:
            acc_arr[r2 + 1][c2 + 1] += degree * type
    for x in range(N):
        for y in range(1, M):
            acc_arr[x][y] = acc_arr[x][y] + acc_arr[x][y - 1]
    for y in range(M):
        for x in range(1, N):
            acc_arr[x][y] = acc_arr[x][y] + acc_arr[x - 1][y]
    ans = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] + acc_arr[x][y] > 0:
                ans += 1
    return ans
