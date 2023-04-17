def check(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True


def go(p):
    if not p:
        return ''
    cnt1, cnt2 = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2 != 0:
            break
    u, v = p[:i + 1], p[i + 1:]
    res = go(v)
    if check(u):
        return u + res
    else:
        u = u[1:-1]
        nu = ''
        for c in u:
            nu += '(' if c == ')' else ')'
        return '(' + res + ')' + nu


def solution(p):
    if not p:
        return p
    if check(p):
        return p
    ans = go(p)
    return ans
