import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]


def move(m, k):
    m = [row[:] for row in m]
    merged = [[False] * N for _ in range(N)]

    if k == 0:
        for y in range(N):
            last_x = -1
            for x in range(N):
                if m[x][y] == 0:
                    continue
                tmp = m[x][y]
                m[x][y] = 0
                if last_x >= 0 and m[last_x][y] == tmp and not merged[last_x][y]:
                    m[last_x][y] *= 2
                    merged[last_x][y] = True
                else:
                    last_x += 1
                    m[last_x][y] = tmp

    elif k == 1:
        for y in range(N):
            last_x = N
            for x in range(N - 1, -1, -1):
                if m[x][y] == 0:
                    continue
                tmp = m[x][y]
                m[x][y] = 0
                if last_x < N and m[last_x][y] == tmp and not merged[last_x][y]:
                    m[last_x][y] *= 2
                    merged[last_x][y] = True
                else:
                    last_x -= 1
                    m[last_x][y] = tmp

    elif k == 2:
        for x in range(N):
            last_y = -1
            for y in range(N):
                if m[x][y] == 0:
                    continue
                tmp = m[x][y]
                m[x][y] = 0
                if last_y >= 0 and m[x][last_y] == tmp and not merged[x][last_y]:
                    m[x][last_y] *= 2
                    merged[x][last_y] = True
                else:
                    last_y += 1
                    m[x][last_y] = tmp

    else:
        for x in range(N):
            last_y = N
            for y in range(N - 1, -1, -1):
                if m[x][y] == 0:
                    continue
                tmp = m[x][y]
                m[x][y] = 0
                if last_y < N and m[x][last_y] == tmp and not merged[x][last_y]:
                    m[x][last_y] *= 2
                    merged[x][last_y] = True
                else:
                    last_y -= 1
                    m[x][last_y] = tmp

    return m


def go(n, m):
    if n == 5:
        return max(max(row) for row in m)
    res = 0
    for k in range(4):
        res = max(res, go(n + 1, move(m, k)))
    return res


ans = go(0, m)
print(ans)
