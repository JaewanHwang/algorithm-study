# 풀이1 1: 누적합 O(24 * 3600 * 1000 + N)
from itertools import accumulate


def solution(lines):
    acc_arr = [0] * (24 * 60 * 60 * 1000 + 1)
    for line in lines:
        _, end, time = line.split()
        end = int(end[:2]) * 60 * 60 * 1000 + int(end[3:5]) * 60 * 1000 + int(end[6:8]) * 1000 + int(end[9:])
        start = max(0, end + 1 - int(float(time[:-1]) * 1000) - 1000 + 1)
        acc_arr[start] += 1
        acc_arr[end + 1] -= 1
    ans = max(accumulate(acc_arr))
    return ans


# 풀이 2: 이분 탐색 O(NlogN)
import bisect


def solution(lines):
    start_l = []
    end_l = []
    candidate_l = []
    for line in lines:
        _, end, time = line.split()
        end = int(end[:2]) * 60 * 60 * 1000 + int(end[3:5]) * 60 * 1000 + int(end[6:8]) * 1000 + int(end[9:])
        start = max(0, end + 1 - int(float(time[:-1]) * 1000))
        start_l.append(start)
        end_l.append(end)
        candidate_l.append(start)
        candidate_l.append(end)
    start_l.sort()
    end_l.sort()
    ans = 0
    for start in candidate_l:
        end = start + 1000 - 1
        e = bisect.bisect_right(start_l, end)
        s = bisect.bisect_left(end_l, start)
        ans = max(ans, e - s)

    return ans
