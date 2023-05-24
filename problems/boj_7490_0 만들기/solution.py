import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def go(i):
    if i == N - 1:
        last_op = '+'
        last_val = 0
        cur_val = 1
        for i in range(N - 1):
            if ans[i] == ' ':
                cur_val = cur_val * 10 + i + 2
            else:
                if last_op == '+':
                    last_val = last_val + cur_val
                else:
                    last_val = last_val - cur_val
                last_op = ans[i]
                cur_val = i + 2
        if last_op == '+':
            res = last_val + cur_val
        else:
            res = last_val - cur_val
        if res != 0:
            return
        for num in range(1, N + 1):
            print(num, end='')
            if num == N:
                break
            print(ans[num - 1], end='')
        print()
        return
    for op in (' ', '+', '-'):
        ans[i] = op
        go(i + 1)


T = int(input())
for _ in range(T):
    N = int(input())
    ans = [''] * (N - 1)
    go(0)
    print()
