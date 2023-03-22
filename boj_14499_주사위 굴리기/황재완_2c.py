import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
N, M, x, y, K, = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(lambda x: int(x) - 1, input().split()))
d = [0] * 7
for op in operations:
    nx, ny = x + dx[op], y + dy[op]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    if op == 0:
        d[4], d[1], d[3], d[6] = d[6], d[4], d[1], d[3]
    elif op == 1:
        d[4], d[1], d[3], d[6] = d[1], d[3], d[6], d[4]
    elif op == 2:
        d[2], d[1], d[5], d[6] = d[1], d[5], d[6], d[2]
    else:
        d[2], d[1], d[5], d[6] = d[6], d[2], d[1], d[5]

    if m[nx][ny] == 0:
        m[nx][ny] = d[6]
    else:
        d[6] = m[nx][ny]
        m[nx][ny] = 0
    x, y = nx, ny
    print(d[1])
