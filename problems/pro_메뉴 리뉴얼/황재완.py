from collections import Counter, defaultdict
import heapq
from itertools import combinations


def solution(orders, course):
    counter = Counter()
    for order in orders:
        for r in course:
            for case in combinations(order, r=r):
                case = ''.join(sorted(case))
                counter[case] += 1

    most_common = defaultdict(list)
    list(map(lambda x: heapq.heappush(most_common[len(x)], (-counter[x], x)),
             filter(lambda x: counter[x] >= 2, counter)))
    ans = []
    for key in most_common:
        max_cnt, case = heapq.heappop(most_common[key])
        max_cnt = -max_cnt
        ans.append(case)
        while most_common[key]:
            cnt, case = heapq.heappop(most_common[key])
            cnt = -cnt
            if cnt == max_cnt:
                ans.append(case)
            else:
                break
    return sorted(ans)
