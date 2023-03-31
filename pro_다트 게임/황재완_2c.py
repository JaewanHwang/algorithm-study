import re


def solution(dartResult):
    i = 0
    ans = []
    bonus_map = {'S': 1, 'D': 2, 'T': 3}
    for result in re.findall(r'\d+[SDT][*#]?', dartResult):
        i = 1
        if result[:2] == '10':
            i = 2
        cur = int(result[:i]) ** bonus_map[result[i]]
        i += 1
        if i == len(result) - 1:
            if result[i] == '*':
                if ans:
                    ans[-1] *= 2
                cur *= 2
            else:
                cur *= -1
        ans.append(cur)
    return sum(ans)
