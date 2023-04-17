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
    for w in kn.split('0'):
        if w.isdigit() and is_prime(int(w)):
            ans += 1

    return ans



