def solution(board, moves):
    ans = 0
    basket = []
    for move in moves:
        y = move - 1
        for x in range(len(board)):
            if board[x][y] > 0:
                if basket and basket[-1] == board[x][y]:
                    basket.pop()
                    ans += 2
                else:
                    basket.append(board[x][y])
                board[x][y] = 0
                break

    return ans