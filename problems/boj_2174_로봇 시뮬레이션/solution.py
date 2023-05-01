import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
change_dir = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
A, B = map(int, input().split())
N, M = map(int, input().split())
m = [[0] * B for _ in range(A)]
robot = [0] * (N + 1)
for ri in range(1, N + 1):
    x, y, dir = input().split()
    x = int(x) - 1
    y = int(y) - 1
    robot[ri] = [x, y, change_dir[dir]]
    m[x][y] = ri

for _ in range(M):
    ri, op, repeat = input().split()
    ri, repeat = int(ri), int(repeat)
    x, y, d = robot[ri]
    if op == 'F':
        nx, ny = x, y
        for _ in range(repeat):
            nx, ny = nx + dx[d], ny + dy[d]
            if nx < 0 or nx >= A or ny < 0 or ny >= B:
                print(f'Robot {ri} crashes into the wall')
                sys.exit(0)
            if m[nx][ny] > 0:
                print(f'Robot {ri} crashes into robot {m[nx][ny]}')
                sys.exit(0)
        m[x][y] = 0
        robot[ri][:2] = [nx, ny]
        m[nx][ny] = ri
    else:
        repeat = repeat % 4
        if op == 'L':
            nd = (d - 1 * repeat) % 4
        else:
            nd = (d + 1 * repeat) % 4
        robot[ri][2] = nd

print('OK')
