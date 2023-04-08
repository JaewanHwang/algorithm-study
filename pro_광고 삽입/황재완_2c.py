from itertools import accumulate


def calculate_time(t):
    return 60 * 60 * int(t[:2]) + 60 * int(t[3:5]) + int(t[6:])


def solution(play_time, adv_time, logs):
    play_time = calculate_time(play_time)
    adv_time = calculate_time(adv_time)
    acc = [0] * (play_time + 1)
    for log in logs:
        start, end = log.split('-')
        start = calculate_time(start)
        end = calculate_time(end)
        acc[start] += 1
        acc[end] -= 1
    acc = list(accumulate(accumulate(acc)))
    ans_time, ans = 0, 0
    for t in range(play_time):
        if t + adv_time - 1 > play_time:
            break
        res = acc[t + adv_time - 1] - (acc[t - 1] if at > 0 else 0)
        if res > ans_time:
            ans = t
            ans_time = res
    print(ans_time)
    hour = ans // (60 * 60)
    minute = (ans % (60 * 60)) // 60
    second = ans % 60
    ans = f'{hour:02}:{minute:02}:{second:02}'
    return ans
