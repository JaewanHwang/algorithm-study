from collections import deque


def solution(menu, order, k):
    q = deque()
    order = order[::-1]
    t, ans = 0, 0
    while q or order:
        if q and q[0] == t:
            q.popleft()
        if t % k == 0 and order:
            o = order.pop()
            q.append(menu[o] + q[-1] if q else t + menu[o])
            ans = max(ans, len(q))
        t += 1
    return ans
