import sys

sys.setrecursionlimit(10 ** 6)


def go(s, e, bt, dummy):
    if s > e:
        return False

    mid = (s + e) // 2
    if bt[mid] == '0':
        dummy = True
    elif bt[mid] == '1' and dummy:
        return False

    if s == e:
        return True

    if not go(s, mid - 1, bt, dummy) or not go(mid + 1, e, bt, dummy):
        return False

    return True


def evaluate(bn):
    for i in range(len(bn) // 2 + 1):
        if bn[i] == '0':
            continue
        bt = bn.zfill(2 * (len(bn) - i) - 1)
        if go(0, len(bt) - 1, bt, False):
            return 1
    return 0


def solution(numbers):
    ans = [0] * len(numbers)
    for i, number in enumerate(numbers):
        bn = bin(number)[2:]
        ans[i] = evaluate(bn)
    return ans


print(solution([63, 111, 95]))
