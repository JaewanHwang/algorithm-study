# 누적합 사용 시 효율성 극대
def solution(N, stages):
    fail_rate = [0] * N
    visit = [0] * (N + 2)
    not_clear = [0] * (N + 2)
    for stage in stages:
        not_clear[stage] += 1

    visit[N + 1] = not_clear[N + 1]
    for stage in range(N, 0, -1):
        visit[stage] = visit[stage + 1] + not_clear[stage]

    for i in range(1, N + 1):
        fail_rate[i - 1] = (not_clear[i] / visit[i] if visit[i] > 0 else 0, i)

    fail_rate.sort(key=lambda x: (-x[0], i))
    answer = list(map(lambda x: x[1], fail_rate))

    return answer