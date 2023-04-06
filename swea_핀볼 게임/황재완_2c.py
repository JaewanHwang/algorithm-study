import sys

sys.stdin = open("input.txt", "r")
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
change_dir = {
    1: [2, 3, 1, 0],
    2: [1, 3, 0, 2],
    3: [3, 2, 0, 1],
    4: [2, 0, 3, 1],
    5: [2, 3, 0, 1]
}


def go(sx, sy, d, cnt):
    x, y = sx, sy
    while True:
        nx, ny = x + dx[d], y + dy[d]
        nd = d
        if 0 <= nx < N and 0 <= ny < N:
            if m[nx][ny] != 0:
                if 1 <= m[nx][ny] <= 5:
                    if change_dir[m[nx][ny]][nd] == (nd + 2) % 4:
                        return cnt * 2 + 1
                    cnt += 1
                    nd = change_dir[m[nx][ny]][nd]
                elif 6 <= m[nx][ny] <= 10:
                    nx, ny = wormholes[(nx, ny)]
                else:
                    return cnt
        else:
            return 2 * cnt + 1
        if (sx, sy) == (nx, ny):
            return cnt
        x, y, d = nx, ny, nd


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
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
    ans = 0
    for x in range(N):
        for y in range(N):
            if m[x][y] == 0:
                for d in range(4):
                    ans = max(ans, go(x, y, d, 0))
    print(f'#{test_case} {ans}')
