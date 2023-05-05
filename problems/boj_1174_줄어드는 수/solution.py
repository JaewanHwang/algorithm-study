import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def go(last, cur, n):
    res.add(cur)
    for nxt in range(last + 1, 10):
        go(nxt, nxt * (10 ** n) + cur, n + 1)


N = int(input())
res = set()
go(-1, 0, 0)
print(sorted(res)[N - 1] if len(res) >= N else -1)
