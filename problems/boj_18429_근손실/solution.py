import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))
used = [False] * N
ans = 0


def go(i, tot):
    global ans
    if i == N:
        ans += 1
        return
    tot -= K
    for k in range(N):
        if used[k]:
            continue
        if a[k] + tot >= 500:
            used[k] = True
            go(i + 1, a[k] + tot)
            used[k] = False


go(0, 500)
print(ans)
