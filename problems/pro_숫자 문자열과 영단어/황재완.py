def solution(s):
    answer = 0
    wdd = dict([('zero', 0), ('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7),
                ('eight', 8), ('nine', 9)])
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer = answer * 10 + int(s[i])
            i += 1
            continue
        for j in range(3, 6):
            if s[i: i + j] in wdd:
                answer = answer * 10 + wdd[s[i: i + j]]
                i += j
                break

    return answer