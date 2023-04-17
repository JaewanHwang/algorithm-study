def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solution(w, h):
    res = gcd(w, h)
    w1 = w // res
    h1 = h // res - 1

    return w * h - (w1 + h1) * res
