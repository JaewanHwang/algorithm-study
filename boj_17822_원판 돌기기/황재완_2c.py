import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 0), (0, 1)
N, M, T = map(int, input().split())
m = [[0] * M] + [list(map(int, input().split())) for _ in range(N)]


def rotate(i):
    if di == 0:
        m[i] = m[i][M - ki:] + m[i][:M - ki]
    else:
        m[i] = m[i][ki:] + m[i][:ki]


def simulate():
    for i in range(1, N + 1):
        if i % xi == 0:
            rotate(i)
    removed = set()
    tot, cnt = 0, 0
    for i in range(1, N + 1):
        for j in range(M):
            if m[i][j] == 0:
                continue
            tot += m[i][j]
            cnt += 1
            for k in range(2):
                ni, nj = i + dx[k], (j + dy[k]) % M
                if m[ni][nj] == m[i][j]:
                    removed.add((i, j))
                    removed.add((ni, nj))
    if not removed:
        if cnt == 0:
            return True
        avg = tot / cnt
        for i in range(1, N + 1):
            for j in range(M):
                if m[i][j] == 0:
                    continue
                if m[i][j] > avg:
                    m[i][j] -= 1
                elif m[i][j] < avg:
                    m[i][j] += 1
    else:
        for i, j in removed:
            m[i][j] = 0
    return False


for _ in range(T):
    xi, di, ki = map(int, input().split())
    if simulate():
        break
ans = 0
for x in range(1, N + 1):
    for y in range(M):
        ans += m[x][y]
print(ans)
