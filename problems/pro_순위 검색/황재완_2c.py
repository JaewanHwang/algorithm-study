import bisect


def solution(info, query):
    m = {l: {p: {c: {d: [] for d in ('chicken', 'pizza', '-')} for c in ('junior', 'senior', '-')} for p in
             ('frontend', 'backend', '-')} for l in ('cpp', 'java', 'python', '-')}
    for el in info:
        l, p, c, d, s = el.split()
        s = int(s)
        for i1 in (l, '-'):
            for i2 in (p, '-'):
                for i3 in (c, '-'):
                    for i4 in (d, '-'):
                        m[i1][i2][i3][i4].append(s)
    for l in ('cpp', 'java', 'python', '-'):
        for p in ('frontend', 'backend', '-'):
            for c in ('junior', 'senior', '-'):
                for d in ('chicken', 'pizza', '-'):
                    m[l][p][c][d].sort()
    ans = []
    for q in query:
        l, p, c, rest = q.split(' and ')
        d, s = rest.split()
        s = int(s)
        ans.append(len(m[l][p][c][d]) - bisect.bisect_left(m[l][p][c][d], s))
    return ans
