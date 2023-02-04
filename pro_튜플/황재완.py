def solution(s):
    answer = []
    c = set()
    s = s[1:len(s) - 1]
    a = s.split('},')
    a.sort(key=lambda x: len(x))
    for el in a:
        el = el.lstrip('{')
        el = el.rstrip('}')
        el = map(int, el.split(','))
        for d in el:
            if d not in c:
                c.add(d)
                answer.append(d)
    return answer

