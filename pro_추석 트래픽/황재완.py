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
