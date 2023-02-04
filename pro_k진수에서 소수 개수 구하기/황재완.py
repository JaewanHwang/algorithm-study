import re


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    ans = 0
    kn = ''
    while n > 0:
        mod = n % k
        kn += str(mod)
        n //= k
    kn = kn[:len(kn)][::-1]
    kn = '0' + kn + '0'
    print(kn)
    p = re.compile('0([1-9]+)(?=0)')
    for d in p.findall(kn):
        print(d)
        if is_prime(int(d)):
            ans += 1

    return ans



