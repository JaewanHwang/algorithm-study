def solution(cap, n, deliveries, pickups):
    dq, pq = [(i, delivery) for i, delivery in enumerate(deliveries, start=1) if delivery > 0], [(i, pickup) for
                                                                                                 i, pickup in
                                                                                                 enumerate(pickups,
                                                                                                           start=1) if
                                                                                                 pickup > 0]
    ans = 0
    while dq or pq:
        cur_d, cur_p = 0, 0
        ans += max(dq[-1][0] if dq else 0, pq[-1][0] if pq else 0) * 2
        while dq and cur_d < cap:
            i, d = dq.pop()
            if d + cur_d > cap:
                dq.append((i, d - (cap - cur_d)))
                break
            else:
                cur_d += d
        while pq and cur_p < cap:
            i, p = pq.pop()
            if p + cur_p > cap:
                pq.append((i, p - (cap - cur_p)))
                break
            else:
                cur_p += p
    return ans
