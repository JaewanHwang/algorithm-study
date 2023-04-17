def solution(n, info):
    max_diff, ans = 1, [0] * 11
    for case in range(1 << 10):
        res = [0] * 11
        apeach_score, ryan_score, rest = 0, 0, n
        failed = False
        for i in range(10):
            if case & (1 << i):  # 이겨야한다
                if rest >= info[i] + 1:
                    rest -= info[i] + 1
                    ryan_score += 10 - i
                    res[i] = info[i] + 1
                else:
                    failed = True
                    break
            else:
                if info[i] > 0:
                    apeach_score += 10 - i
        if not failed:
            if rest > 0:
                res[10] += rest
            diff = ryan_score - apeach_score
            if diff <= 0:
                continue
            if diff > max_diff:
                max_diff, ans = diff, res
            elif diff == max_diff:
                for i in range(10, -1, -1):
                    if res[i] < ans[i]:
                        break
                    elif res[i] > ans[i]:
                        ans = res
                        break

    return ans if sum(ans) == n else [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
