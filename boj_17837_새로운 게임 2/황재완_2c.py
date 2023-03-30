import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
N, K = map(int, input().split())
pieces = []
m = [[[] for _ in range(N)] for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]
for pi in range(K):
    x, y, d = map(lambda x: int(x) - 1, input().split())
    pieces.append([x, y, d])
    m[x][y].append(pi)
change_dir = [1, 0, 3, 2]


def get_moved_pieces(nx, ny, p):
    x, y, _ = pieces[p]
    pi = m[x][y].index(p)
    move = m[x][y][pi:]
    m[x][y] = m[x][y][:pi]
    for pi in move:
        pieces[pi][0], pieces[pi][1] = nx, ny
    return move


def go_white(nx, ny, p):
    move = get_moved_pieces(nx, ny, p)
    m[nx][ny].extend(move)
    if len(m[nx][ny]) >= 4:
        return True
    return False


def go_red(nx, ny, p):
    move = get_moved_pieces(nx, ny, p)
    m[nx][ny].extend(move[::-1])
    if len(m[nx][ny]) >= 4:
        return True
    return False


def go_blue(p):
    x, y, d = pieces[p]
    nd = change_dir[d]
    nx, ny = x + dx[nd], y + dy[nd]
    pieces[p][2] = nd
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 0:
            return go_white(nx, ny, p)
        elif board[nx][ny] == 1:
            return go_red(nx, ny, p)
    return False


def simulate():
    for p in range(K):
        x, y, d = pieces[p]
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == 0:
                res = go_white(nx, ny, p)
            elif board[nx][ny] == 1:
                res = go_red(nx, ny, p)
            else:
                res = go_blue(p)
        else:
            res = go_blue(p)
        if res:
            return True
    return False


for ans in range(1, 1002):
    if simulate():
        break

print(ans if ans != 1001 else -1)
