import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
t = [False] * N
def calculate(a, b):
    ta, tb = 0, 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            ta += S[a[i]][a[j]] + S[a[j]][a[i]]
            tb += S[b[i]][b[j]] + S[b[j]][b[i]]
    return abs(ta - tb)
def go(n):
    if n == N:
        a, b = [], []
        for i in range(N):
            if t[i]:
                a.append(i)
            else:
                b.append(i)
        return calculate(a, b) if len(a) == len(b) else float('inf')
    t[n] = True
    res = go(n + 1)
    t[n] = False
    return min(res, go(n + 1))

ans = go(0)
print(ans)