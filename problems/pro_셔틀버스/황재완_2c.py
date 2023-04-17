from collections import deque


def solution(n, t, m, timetable):
    q = []
    for time in timetable:
        time = int(time[:2]) * 60 + int(time[3:])
        q.append(time)
    q = deque(sorted(q))
    ans = 0
    for arrival_time in range(9 * 60, min(24 * 60, 9 * 60 + n * t), t):
        cnt = 0
        while q and cnt < m:
            if q[0] > arrival_time:
                break
            ans = q.popleft() - 1
            cnt += 1
    if cnt < m:
        ans = arrival_time
    return f'{ans // 60:02}:{ans % 60:02}'
