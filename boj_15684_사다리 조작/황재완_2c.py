import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [list(range(N)) for _ in range(H)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    ladder[a][b] = b + 1
    ladder[a][b + 1] = b


def simulate(n):
    global ans
    for sb in range(N):
        b = sb
        for a in range(H):
            b = ladder[a][b]
        if b != sb:
            return
    ans = min(ans, n)


def go(n, start):
    if n >= ans or n > 3:
        return
    simulate(n)
    for i in range(start, H * (N - 1)):
        a, b = i // (N - 1), i % (N - 1)
        if ladder[a][b] == b and ladder[a][b + 1] == b + 1:
            ladder[a][b] = b + 1
            ladder[a][b + 1] = b
            go(n + 1, i + 1)
            ladder[a][b] = b
            ladder[a][b + 1] = b + 1


ans = N * H
go(0, 0)
print(ans if ans != N * H else -1)
