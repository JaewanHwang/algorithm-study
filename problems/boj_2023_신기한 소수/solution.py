import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())


# SIZE = 10 ** N
# prime = [True] * (SIZE)
# prime[0] = prime[1] = False
# for i in range(2, SIZE):
#     if i * i > SIZE:
#         break
#     if not prime[i]:
#         continue
#     for j in range(i * i, SIZE, i):
#         prime[j] = False


def is_prime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    for k in range(2, n + 1):
        if k * k > n:
            break
        if n % k == 0:
            return False
    return True


def go(i, n):
    if i == N:
        print(n)
        return
    for j in range(10) if i >= 1 else range(1, 10):
        res = n * 10 + j
        if is_prime(res):
            go(i + 1, res)


go(0, 0)
