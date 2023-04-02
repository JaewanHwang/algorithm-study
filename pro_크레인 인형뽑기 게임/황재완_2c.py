def solution(board, moves):
    ans = 0
    stack = []
    for y in moves:
        y -= 1
        for x in range(len(board)):
            if board[x][y] > 0:
                if stack and stack[-1] == board[x][y]:
                    ans += 2
                    stack.pop()
                else:
                    stack.append(board[x][y])
                board[x][y] = 0
                break
    return ans
