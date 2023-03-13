import sys

sys.stdin = open("sample_input.txt", "r")
dx, dy = (-1, 0, 0, 1), (0, -1, 1, 0)
dir_map = {1: {3: 2, 1: 0},
           2: {1: 3, 0: 2},
           3: {2: 3, 0: 1},
           4: {2: 0, 3: 1},
           5: {}}


def simulate():
    ans = 0
    tmp = [[] for _ in range(11)]
    for x in range(N):
        for y in range(N):
            if 6 <= m[x][y] <= 10:
                tmp[m[x][y]].append((x, y))
    wormholes = dict()
    for i in range(6, 11):
        if tmp[i]:
            wormholes[tmp[i][0]] = tmp[i][1]
            wormholes[tmp[i][1]] = tmp[i][0]
    for x in range(N):
        for y in range(N):
            if m[x][y] == 0:
                for k in range(4):
                    ans = max(ans, go(x, y, k, wormholes))
    return ans


def go(sx, sy, k, wormholes):
    score = 0
    x, y = sx, sy
    d = k
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if 1 <= m[nx][ny] <= 5:
                if d in dir_map[m[nx][ny]]:
                    score += 1
                    d = dir_map[m[nx][ny]][d]
                    x, y = nx, ny
                else:
                    return score * 2 + 1
            elif 6 <= m[nx][ny] <= 10:
                x, y = wormholes[(nx, ny)]
            else:
                x, y = nx, ny
            if (x, y) == (sx, sy) or m[x][y] == -1:
                return score
        else:
            return score * 2 + 1


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {simulate()}')
