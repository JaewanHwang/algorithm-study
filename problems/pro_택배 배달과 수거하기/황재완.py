def solution(cap, n, deliveries, pickups):
    houses_to_deliver = []
    houses_to_pickup = []
    for i in range(n):
        if deliveries[i] > 0:
            houses_to_deliver.append(i)
        if pickups[i] > 0:
            houses_to_pickup.append(i)
    ans = 0
    di, pi = len(houses_to_deliver) - 1, len(houses_to_pickup) - 1
    while di >= 0 or pi >= 0:
        deliver = cap
        deliver_last = houses_to_deliver[di] if di >= 0 else 0
        while deliver > 0 and di >= 0:
            d = min(deliver, deliveries[houses_to_deliver[di]])
            deliveries[houses_to_deliver[di]] -= d
            deliver -= d
            if deliveries[houses_to_deliver[di]] <= deliver:
                di -= 1

        pickup = cap
        pickup_last = houses_to_pickup[pi] if pi >= 0 else 0
        while pickup > 0 and pi >= 0:
            p = min(pickup, pickups[houses_to_pickup[pi]])
            pickups[houses_to_pickup[pi]] -= p
            pickup -= p
            if pickups[houses_to_pickup[pi]] <= pickup:
                pi -= 1

        ans += (max(deliver_last, pickup_last) + 1) * 2
    return ans
