def solution(dartResult):
    i = 0
    ans = []
    bonus_map = {'S': 1, 'D': 2, 'T': 3}
    while i < len(dartResult):
        if dartResult[i + 1].isdigit():
            i += 1
            cur = 10 ** bonus_map[dartResult[i + 1]]
        else:
            cur = int(dartResult[i]) ** bonus_map[dartResult[i + 1]]
        i += 2
        if i < len(dartResult) and not dartResult[i].isdigit():
            if dartResult[i] == '*':
                if len(ans) > 0:
                    ans[-1] *= 2
                cur *= 2
            else:
                cur *= -1
            i += 1
        ans.append(cur)
    return sum(ans)
