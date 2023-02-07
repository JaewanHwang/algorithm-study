from collections import Counter
import heapq


def solution(gems):
    ans = []
    TOTAL_CNT = len(Counter(gems))
    gem_set = set()
    gem_counter = dict()
    l, r = 0, 0
    while l <= r and r < len(gems):
        if gems[r] not in gem_set:
            gem_counter[gems[r]] = 1
            gem_set.add(gems[r])
        else:
            gem_counter[gems[r]] += 1
        if len(gem_set) == TOTAL_CNT:
            heapq.heappush(ans, (r - l, l))
            while gem_counter[gems[l]] - 1 >= 1:
                gem_counter[gems[l]] -= 1
                l += 1
                heapq.heappush(ans, (r - l, l))
        r += 1

    d, l = heapq.heappop(ans)
    return [l + 1, d + l + 1]

