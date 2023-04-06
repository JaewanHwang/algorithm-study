def go(sx, sy, key, lock, N, M, HOLE):
    cnt = 0
    for x in range(sx, sx + M):
        for y in range(sy, sy + M):
            if 0 <= x < N and 0 <= y < N:
                if lock[x][y] ^ key[x - sx][y - sy] == 1:
                    if lock[x][y] == 0:
                        cnt += 1
                else:
                    return False
    if cnt == HOLE:
        return True
    return False


def solution(key, lock):
    N, M = len(lock), len(key)
    HOLE = 0
    for x in range(N):
        for y in range(N):
            if lock[x][y] == 0:
                HOLE += 1
    patterns = [key]
    for _ in range(3):
        tkey = [[0] * M for _ in range(M)]
        for x in range(M):
            for y in range(M):
                tkey[x][y] = patterns[-1][M - 1 - y][x]
        patterns.append(tkey)
    for sx in range(-M + 1, N):
        for sy in range(-M + 1, N):
            for key in patterns:
                if go(sx, sy, key, lock, N, M, HOLE):
                    return True
    return False
