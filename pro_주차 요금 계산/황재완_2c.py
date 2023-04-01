import math


def solution(fees, records):
    history = dict()
    for record in records:
        time, num, op = record.split()
        time = int(time[:2]) * 60 + int(time[3:])
        if num not in history:
            history[num] = [0, -1]
        if op == 'IN':
            history[num][1] = time
        else:
            history[num][0] += time - history[num][1]
            history[num][1] = -1
    for num in history:
        tot_time = history[num][0] + (24 * 60 - 1 - history[num][1] if history[num][1] != -1 else 0)
        history[num] = fees[1] + math.ceil(max(0, tot_time - fees[0]) / fees[2]) * fees[3]
    ans = [history[key] for key in sorted(history)]
    return ans
