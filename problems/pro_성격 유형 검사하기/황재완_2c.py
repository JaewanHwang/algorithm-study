def solution(survey, choices):
    counter = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for kind, choice in zip(survey, choices):
        if 1 <= choice <= 3:
            counter[kind[0]] += 4 - choice
        elif 5 <= choice <= 7:
            counter[kind[1]] += choice - 4
    ans = ''
    for a, b in ('RT', 'CF', 'JM', 'AN'):
        ans += max(a, b, key=lambda x: (counter[x], -ord(x)))
    return ans
