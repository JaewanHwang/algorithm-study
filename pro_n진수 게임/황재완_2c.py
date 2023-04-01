def transform(n, num):
    res = []
    while True:
        num, mod = divmod(num, n)
        res.append(hex(mod).upper()[2:])
        if num == 0:
            break
    return res


def solution(n, t, m, p):
    ans, cnt, num, turn, t_num = '', 0, 0, 0, []
    while cnt < t:
        if not t_num:
            t_num = transform(n, num)
            num += 1
        cur = t_num.pop()
        if turn == p - 1:
            ans += cur
            cnt += 1
        turn = (turn + 1) % m
    return ans
