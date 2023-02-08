def go(w):
    if w == '':
        return w
    u, v = '', ''
    l, r = 0, 0
    for c in w:
        if c == '(':
            l += 1
        else:
            r += 1
        u += c
        if l == r:
            break
    v = w[l + r:]
    if evaluate(u):
        return u + go(v)
    else:
        return '(' + go(v) + ')' + ''.join(map(lambda x: '(' if x == ')' else ')', u[1:len(u) - 1]))


def evaluate(w):
    stack = []
    for c in w:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True


def solution(p):
    if evaluate(p):
        return p
    return go(p)