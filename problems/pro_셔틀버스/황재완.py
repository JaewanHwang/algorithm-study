import bisect


def ok(mid, me, n, m, t, sorted_timetable):
    board_cnt = 0
    for i in range(n):
        bus_arrival_time = 60 * 9 + i * t
        if bus_arrival_time >= 60 * 24:
            return False
        for _ in range(m):
            if board_cnt == me and bus_arrival_time >= mid:
                return True
            if board_cnt == len(sorted_timetable) or sorted_timetable[board_cnt] > bus_arrival_time:
                break
            board_cnt += 1
    return False


def solution(n, t, m, timetable):
    sorted_timetable = []
    for crew_arrival_time in timetable:
        hh, mm = crew_arrival_time.split(':')
        sorted_timetable.append(int(hh) * 60 + int(mm))
    sorted_timetable.sort()
    l, r = 0, 24 * 60 - 1
    while l <= r:
        mid = (l + r) // 2
        me = bisect.bisect_right(sorted_timetable, mid)
        if ok(mid, me, n, m, t, sorted_timetable):
            l = mid + 1
        else:
            r = mid - 1
    ans = str((l - 1) // 60).zfill(2) + ':' + str((l - 1) % 60).zfill(2)
    return ans
