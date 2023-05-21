import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())
a = list(map(int, input().split()))
bt = [0] * (2 ** K + 1)


def go(i):
    global cnt
    lc, rc = 2 * i, 2 * i + 1
    if lc < 2 ** K:
        go(lc)
    bt[i] = a[cnt]
    cnt += 1
    if rc < 2 ** K:
        go(rc)


cnt = 0
go(1)
for level in range(1, K + 1):
    print(*bt[2 ** (level - 1): 2 ** level])
