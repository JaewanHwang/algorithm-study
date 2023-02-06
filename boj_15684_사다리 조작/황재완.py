import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, H = map(int, input().split())
c = [[False] * (N - 1) for _ in range(H)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    c[a][b] = True


def go(n, cnt):
    if cnt == ans:
        return simulate()
    for i in range(n, (N - 1) * H):
        x, y = i // (N - 1), i % (N - 1)
        if c[x][y] or (y - 1 >= 0 and c[x][y - 1]) or (y + 1 < N - 1 and c[x][y + 1]):
            continue
        c[x][y] = True
        if go(i + 1, cnt + 1):
            return True
        c[x][y] = False
    return False


def simulate():
    for n in range(N):
        y = n
        for x in range(H):
            if y < N - 1 and c[x][y]:
                y += 1
            elif y - 1 >= 0 and c[x][y - 1]:
                y -= 1
        if y != n:
            return False
    return True


for ans in range(4):
    if go(0, 0):
        print(ans)
        sys.exit(0)
print(-1)
