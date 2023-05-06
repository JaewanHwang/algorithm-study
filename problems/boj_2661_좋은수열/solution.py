import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
ans = [0] * N


def check(i, n):
    for l in range(1, i + 1):
        if i - 2 * l + 1 < 0:
            break
        if ans[i - l + 1: i + 1] == ans[i - 2 * l + 1: i - l + 1]:
            return False
    return True


def go(i, last):
    if i == N:
        return True
    for n in ('1', '2', '3'):
        ans[i] = n
        if check(i, n):
            if go(i + 1, n):
                return True
    return False


go(0, '0')
print(''.join(ans))
