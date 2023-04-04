def ok(mid, stones, k):
    cnt = 0
    for stone in stones:
        if stone < mid:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True


def solution(stones, k):
    l, r = 0, max(stones)
    while l <= r:
        mid = (l + r) // 2
        if ok(mid, stones, k):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
