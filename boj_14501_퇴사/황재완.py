import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
d = [-1] * (N + 1)
d[N] = 0


def go(n):
    if d[n] != -1:
        return d[n]
    d[n] = go(n + 1)
    if a[n][0] + n <= N:
        d[n] = max(d[n], a[n][1] + go(n + a[n][0]))
    return d[n]


ans = go(0)

print(ans)
