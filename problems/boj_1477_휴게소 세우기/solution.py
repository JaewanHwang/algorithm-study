import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, L = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a.append(L)


def ok(k):
    cnt = 0
    cur = 0
    for d in a:
        if d - cur > k:
            cnt += (d - cur) // k + (0 if (d - cur) % k != 0 else -1)
        cur = d
    if cnt <= M:
        return True
    else:
        return False


l, r = 1, L

while l <= r:
    k = (l + r) // 2
    if ok(k):
        ans = k
        r = k - 1
    else:
        l = k + 1

print(ans)
