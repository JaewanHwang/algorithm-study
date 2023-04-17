def transform_to_n(n, num):
    res = ''
    while True:
        div, mod = divmod(num, n)
        res += chr(mod + 55) if 10 <= mod <= 15 else str(mod)
        if div == 0:
            break
        num //= n
    return res[::-1]


def solution(n, t, m, p):
    p -= 1
    answer = ''
    cp = cn = ci = 0
    tcn = transform_to_n(n, cn)

    while len(answer) < t:
        if ci == len(tcn):
            cn += 1
            ci = 0
            tcn = transform_to_n(n, cn)
        if cp == p:
            answer += tcn[ci]
        cp = (cp + 1) % m
        ci += 1

    return answer