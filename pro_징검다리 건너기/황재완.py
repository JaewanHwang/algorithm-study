def solution(stones, k):
    nums_pos = dict()
    for pos, stone in enumerate(stones):
        if stone not in nums_pos:
            nums_pos[stone] = []
        nums_pos[stone].append(pos + 1)
    dist = [[1, i - 1, i + 1] for i in range(len(stones) + 2)]  # [dist, prev, next]

    ans = 0
    for num in sorted(nums_pos):
        ans = num
        for cur in nums_pos[num]:
            d, prev, next = dist[cur]
            dist[prev][0] += d
            dist[prev][2], dist[next][1] = next, prev
            if dist[prev][0] > k:
                return ans

    return ans
