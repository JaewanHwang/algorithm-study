import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
sharks = {i: [0] * 3 for i in range(1, M + 1)}
smell = [[0] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if m[x][y]:
            sharks[m[x][y]][:2] = [x, y]
            smell[x][y] = [m[x][y], K]
for i, d in enumerate(map(lambda x: int(x) - 1, input().split()), start=1):
    sharks[i][2] = d
priority = [0] + [[list(map(lambda x: int(x) - 1, input().split())) for _ in range(4)] for _ in range(M)]


def simulate():
    global m

    tm = [[0] * N for _ in range(N)]
    for s in sorted(sharks):
        x, y, d = sharks[s]
        my_smell = None
        for nd in priority[s][d]:
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < N and 0 <= ny < N:
                if not smell[nx][ny]:
                    if tm[nx][ny]:
                        sharks.pop(s)
                    else:
                        tm[nx][ny] = s
                        sharks[s] = [nx, ny, nd]
                    break
                elif smell[nx][ny][0] == s:
                    if not my_smell:
                        my_smell = [nx, ny, nd]
        else:
            tm[my_smell[0]][my_smell[1]] = s
            sharks[s] = my_smell

    for x in range(N):
        for y in range(N):
            if not smell[x][y]:
                continue
            smell[x][y][1] -= 1
            if smell[x][y][1] == 0:
                smell[x][y] = 0

    for s, (x, y, _) in sharks.items():
        smell[x][y] = [s, K]

    m = tm
    return len(sharks) == 1


for ans in range(1, 1_002):
    if simulate():
        break

print(ans if ans != 1_001 else -1)
