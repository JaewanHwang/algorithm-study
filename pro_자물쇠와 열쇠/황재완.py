def rotate(key):
    keys = []
    for _ in range(4):
        tmp_key = [[0] * M for _ in range(M)]
        for x in range(M):
            for y in range(M):
                tmp_key[x][y] = key[M - y - 1][x]
        key = tmp_key
        keys.append([row[:] for row in key])
    return keys


def move(sx, sy, lock):
    for key in all_keys:
        cnt = 0
        tmp_lock = [row[:] for row in lock]
        fail = False
        for x in range(M):
            for y in range(M):
                if x + sx < 0 or x + sx >= N or y + sy < 0 or y + sy >= N:
                    continue
                if key[x][y] == tmp_lock[x + sx][y + sy]:
                    fail = True
                    break
                if key[x][y] == 1 and tmp_lock[x + sx][y + sy] == 0:
                    cnt += 1
            if fail:
                break
        if cnt == TOTAL_BLANK:
            return True
    return False


all_keys, N, M, TOTAL_BLANK = None, 0, 0, 0


def solution(key, lock):
    global all_keys, N, M, TOTAL_BLANK
    N, M = len(lock), len(key)
    all_keys = rotate(key)

    for x in range(N):
        for y in range(N):
            if lock[x][y] == 0:
                TOTAL_BLANK += 1

    for sx in range(-M + 1, N):
        for sy in range(-M + 1, N):
            if move(sx, sy, lock):
                return True

    return False
