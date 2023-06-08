import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

k = int(input())
w = list(map(int, input().split()))
S = sum(w)
possible = [False] * (S + 1)


def go(i, tot):
    if i == k:
        if tot >= 1:
            possible[tot] = True
        return
    go(i + 1, tot + w[i])
    go(i + 1, tot - w[i])
    go(i + 1, tot)


go(0, 0)

ans = 0
for n in range(1, S + 1):
    if not possible[n]:
        ans += 1
print(ans)
