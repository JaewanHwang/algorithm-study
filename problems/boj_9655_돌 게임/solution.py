import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
dp_A = [-1] * 1001
dp_B = [-1] * 1001
dp_A[1] = dp_A[3] = dp_B[1] = dp_B[3] = True


def go_A(n):
    if dp_A[n] != -1:
        return dp_A[n]
    res = [0, 0]
    if n > 1:
        res[1 - go_B(n - 1)] += 1
    if n > 3:
        res[1 - go_B(n - 3)] += 1
    if res[1] > 0:
        dp_A[n] = True
        return True
    else:
        dp_A[n] = False
        return False


def go_B(n):
    if dp_B[n] != -1:
        return dp_B[n]
    res = [0, 0]
    if n > 1:
        res[1 - go_A(n - 1)] += 1
    if n > 3:
        res[1 - go_A(n - 3)] += 1
    if res[1] > 0:
        dp_B[n] = True
        return True
    else:
        dp_B[n] = False
        return False


if go_A(N):
    print('SK')
else:
    print('CY')
