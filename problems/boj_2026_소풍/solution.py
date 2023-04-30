import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
input = sys.stdin.readline

K, N, F = map(int, input().split())
friend = [set() for i in range(N + 1)]
for _ in range(F):
    u, v = map(int, input().split())
    friend[u].add(v)
    friend[v].add(u)


def go(i, n):
    if i == K:
        return True
    for start in range(n, N + 1):
        if not cur <= friend[start]:
            continue
        cur.add(start)
        if go(i + 1, start + 1):
            return True
        cur.remove(start)
    return False


cur = set()
go(0, 1)
if not cur:
    print(-1)
else:
    print(*sorted(cur), sep='\n')
