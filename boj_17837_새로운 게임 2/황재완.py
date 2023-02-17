import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)

N, K = map(int, input().split())
chess_board = [list(map(int, input().split())) for _ in range(N)]
pieces = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]  # x, y, d
m = [[[] for _ in range(N)] for _ in range(N)]
for num, piece in enumerate(pieces):
    x, y, _ = piece
    m[x][y].append(num)


def go_red_or_white(num):
    x, y, d = pieces[num]
    nx, ny = x + dx[d], y + dy[d]

    me_index = m[x][y].index(num)
    for i in range(me_index, len(m[x][y])):
        pieces[m[x][y][i]][0], pieces[m[x][y][i]][1] = nx, ny

    if chess_board[nx][ny] == 1:
        m[nx][ny].extend(m[x][y][me_index:][::-1])
    else:
        m[nx][ny].extend(m[x][y][me_index:])

    if len(m[nx][ny]) >= 4:
        return True

    m[x][y] = m[x][y][:me_index]
    return False


def go_blue(num):
    x, y, d = pieces[num]
    nd = 1 - d if 0 <= d <= 1 else 5 - d
    nx, ny = x + dx[nd], y + dy[nd]
    pieces[num][2] = nd
    if nx < 0 or nx >= N or ny < 0 or ny >= N or chess_board[nx][ny] == 2:
        return False
    elif 0 <= chess_board[nx][ny] <= 1:
        if go_red_or_white(num):
            return True
    return False


def simulate():
    for num in range(K):
        x, y, d = pieces[num]
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or chess_board[nx][ny] == 2:
            if go_blue(num):
                return True
        elif 0 <= chess_board[nx][ny] <= 1:
            if go_red_or_white(num):
                return True
    return False


for ans in range(1, 1002):
    if simulate():
        break

if ans == 1001:
    ans = -1
print(ans)
