from itertools import accumulate


def solution(play_time, adv_time, logs):
    play_time = 60 * 60 * int(play_time[:2]) + 60 * int(play_time[3:5]) + int(play_time[6:])
    adv_time = 60 * 60 * int(adv_time[:2]) + 60 * int(adv_time[3:5]) + int(adv_time[6:])
    acc = [0] * (play_time + 2)

    for log in logs:
        s, e = log.split('-')
        start_time = 60 * 60 * int(s[:2]) + 60 * int(s[3:5]) + int(s[6:])
        end_time = 60 * 60 * int(e[:2]) + 60 * int(e[3:5]) + int(e[6:])
        acc[start_time + 1] += 1
        acc[end_time + 1] -= 1

    acc = list(accumulate(accumulate(acc)))
    max_s, max_acc = 0, 0
    for s in range(play_time - adv_time + 1):
        e = s + adv_time
        if acc[e] - acc[s] > max_acc:
            max_s, max_acc = s, acc[e] - acc[s]

    hh, rest = divmod(max_s, 60 * 60)
    mm, ss = divmod(rest, 60)
    ans = str(hh).zfill(2) + ':' + str(mm).zfill(2) + ':' + str(ss).zfill(2)

    return ans
