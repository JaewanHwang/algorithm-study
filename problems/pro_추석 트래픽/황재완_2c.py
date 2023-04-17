import bisect


def solution(lines):
    starts, ends = [], []
    points = []
    for line in lines:
        _, end, t = line.split()
        end = int(end[:2]) * 60 * 60 * 1000 + int(end[3:5]) * 60 * 1000 + int(end[6:8]) * 1000 + int(end[9:])
        start = end - int(float(t[:-1]) * 1000) + 1
        starts.append(start)
        ends.append(end)
        points.append(start)
        points.append(end)

    starts.sort()
    ends.sort()
    ans = 0
    for point in points:
        e = bisect.bisect_right(starts, point + 999)
        s = bisect.bisect_left(ends, point)
        ans = max(ans, e - s)
    return ans
