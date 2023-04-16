import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
X = int(input())
d = [-1] * (X + 1)
d[1] = 0
a = [-1] * (X + 1)


def go(n):
    if d[n] != -1:
        return d[n]
    d[n] = float('inf')
    if n % 3 == 0:
        res = go(n // 3)
        if d[n] > res:
            d[n] = res
            a[n] = n // 3
    if n % 2 == 0:
        res = go(n // 2)
        if d[n] > res:
            d[n] = res
            a[n] = n // 2
    res = go(n - 1)
    if d[n] > res:
        d[n] = res
        a[n] = n - 1
    d[n] += 1
    return d[n]


ans = go(X)
print(ans)
n = X
ans = [n]
while a[n] != -1:
    ans.append(a[n])
    n = a[n]
print(*ans)
