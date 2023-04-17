import sys

sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
m = [[0] * M for _ in range(N)]


def ok(sx, sy):
    for x in range(sx, sx + R):
        for y in range(sy, sy + C):
            if m[x][y] and sticker[x - sx][y - sy]:
                return False
    return True


def insert(sx, sy):
    for x in range(sx, sx + R):
        for y in range(sy, sy + C):
            m[x][y] ^= sticker[x - sx][y - sy]


def simulate():
    for x in range(N - R + 1):
        for y in range(M - C + 1):
            if ok(x, y):
                insert(x, y)
                return True
    return False


def rotate():
    tmp = [[0] * R for _ in range(C)]
    for x in range(R):
        for y in range(C):
            tmp[y][R - 1 - x] = sticker[x][y]
    return tmp


for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    for i in range(4):
        if i > 0:
            sticker = rotate()
            R, C = C, R
        if simulate():
            break

print(sum(sum(row) for row in m))
