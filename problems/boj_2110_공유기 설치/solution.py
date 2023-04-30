import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, C = map(int, input().split())
a = [int(input()) for _ in range(N)]
a.sort()


def ok(k):
    cnt = 1
    cur = a[0]
    for j in range(1, N):
        if a[j] - cur >= k:
            cnt += 1
            cur = a[j]
    if cnt >= C:
        return True
    else:
        return False


l, r = 1, max(a) - min(a)

while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)
