import sys

sys.stdin = open('input.txt')

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
pipe_map = [[0, 2], [1, 2], [0, 1, 2]]
check_map = [[0, ], [2, ], [0, 2, 1]]
dx, dy = (0, 1, 1), (1, 1, 0)
ans = 0


def go(x, y, state):
    if d[x][y][state] != -1:
        return d[x][y][state]
    res = 0
    for new_state in pipe_map[state]:
        for k in check_map[new_state]:
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or m[nx][ny] == 1:
                break
        else:
            res += go(nx, ny, new_state)
    d[x][y][state] = res
    return d[x][y][state]


d = [[[-1] * 3 for _ in range(N)] for _ in range(N)]

if d[N - 1][N - 1]:
    if d[N - 2][N - 1]:
        d[N - 1][N - 1][1] = 1
    if d[N - 2][N - 1] and d[N - 1][N - 2]:
        d[N - 1][N - 1][2] = 1
    if d[N - 1][N - 2]:
        d[N - 1][N - 1][0] = 1
ans = go(0, 1, 0)
print(ans)
