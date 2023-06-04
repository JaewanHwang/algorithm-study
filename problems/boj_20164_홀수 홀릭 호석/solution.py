import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())


def calculate(num):
    ret = 0
    for digit in num:
        if int(digit) % 2 == 1:
            ret += 1
    return ret


def go(cur, tot):
    global ans_max, ans_min
    tot += calculate(cur)
    if len(cur) == 1:
        ans_max, ans_min = max(ans_max, tot), min(ans_min, tot)
        return
    elif len(cur) == 2:
        go(str(int(cur[0]) + int(cur[1])), tot)
    else:
        for b1 in range(len(cur) - 2):
            for b2 in range(b1 + 1, len(cur) - 1):
                go(str(int(cur[:b1 + 1]) + int(cur[b1 + 1: b2 + 1]) + int(cur[b2 + 1:])), tot)


ans_max, ans_min = 0, float('inf')
go(str(N), 0)
print(ans_min, ans_max)
