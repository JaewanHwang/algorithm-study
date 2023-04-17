def solution(N, stages):
    cnt_stage = [0] * (N + 2)
    for stage in stages:
        cnt_stage[stage] += 1
    cnt_clear = cnt_stage[N + 1]
    fail_rates = []
    for i in range(N, 0, -1):
        cnt_clear += cnt_stage[i]
        fail_rates.append((cnt_stage[i] / cnt_clear if cnt_clear > 0 else 0, i))
    return list(map(lambda x: x[1],
                    sorted(fail_rates, key=lambda x: (-x[0], x[1]))))
