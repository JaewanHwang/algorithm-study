import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
o = [list(map(int, input().split())) for _ in range(N)]
ans = 2


def simulate(d, m, c):
    if d == 0:
        for y in range(N):
            cur = 0
            for x in range(N):
                if m[x][y] == 0:
                    continue
                if cur - 1 >= 0 and m[cur - 1][y] == m[x][y] != 0 and not c[cur - 1][y]:
                    m[cur - 1][y] *= 2
                    m[x][y] = 0
                    c[cur - 1][y] = True
                else:
                    tmp = m[x][y]
                    m[x][y] = 0
                    m[cur][y] = tmp
                    cur += 1
    elif d == 1:
        for y in range(N):
            cur = N - 1
            for x in range(N - 1, -1, -1):
                if m[x][y] == 0:
                    continue
                if cur + 1 < N and m[cur + 1][y] == m[x][y] != 0 and not c[cur + 1][y]:
                    m[cur + 1][y] *= 2
                    m[x][y] = 0
                    c[cur + 1][y] = True
                else:
                    tmp = m[x][y]
                    m[x][y] = 0
                    m[cur][y] = tmp
                    cur -= 1
    elif d == 2:
        for x in range(N):
            cur = 0
            for y in range(N):
                if m[x][y] == 0:
                    continue
                if cur - 1 >= 0 and m[x][cur - 1] == m[x][y] != 0 and not c[x][cur - 1]:
                    m[x][cur - 1] *= 2
                    m[x][y] = 0
                    c[x][cur - 1] = True
                else:
                    tmp = m[x][y]
                    m[x][y] = 0
                    m[x][cur] = tmp
                    cur += 1
    else:
        for x in range(N):
            cur = N - 1
            for y in range(N - 1, -1, -1):
                if m[x][y] == 0:
                    continue
                if cur + 1 < N and m[x][cur + 1] == m[x][y] != 0 and not c[x][cur + 1]:
                    m[x][cur + 1] *= 2
                    m[x][y] = 0
                    c[x][cur + 1] = True
                else:
                    tmp = m[x][y]
                    m[x][y] = 0
                    m[x][cur] = tmp
                    cur -= 1


for case in range(2 ** 10):
    bit = 3
    m = [o[i][:] for i in range(N)]
    for _ in range(5):
        d = case & bit
        simulate(d, m, [[False] * N for _ in range(N)])
        case >>= 2
    ans = max(ans, max(map(max, m)))

print(ans)
