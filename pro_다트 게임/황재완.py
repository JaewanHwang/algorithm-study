def solution(dartResult):
    res = [0]
    for i, ch in enumerate(dartResult):
        if ch.isdigit():
            if i - 1 >= 0 and dartResult[i - 1].isdigit():
                res[cur] = 10
            else:
                res.append(int(ch))
                cur = len(res) - 1
                last = cur - 1
        elif ch.isalpha():
            if ch == 'S':
                res[cur] **= 1
            elif ch == 'D':
                res[cur] **= 2
            elif ch == 'T':
                res[cur] **= 3
        else:
            if ch == '*':
                res[last] *= 2
                res[cur] *= 2
            elif ch == '#':
                res[cur] *= -1
    print(res)
    answer = sum(res)
    return answer