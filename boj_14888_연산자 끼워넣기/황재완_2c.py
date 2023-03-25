import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))
num2op = ['+', '-', '*', '//']
ans_min, ans_max = 1e9, -1e9
map


def go(i, res):
    global ans_min, ans_max
    if i == N - 1:
        ans_max = max(ans_max, res)
        ans_min = min(ans_min, res)
        return
    for opi in range(4):
        if operators[opi] > 0:
            operators[opi] -= 1
            if opi == 3 and res < 0:
                next_res = -(-res // A[i + 1])
            else:
                next_res = eval(str(res) + num2op[opi] + str(A[i + 1]))
            go(i + 1, next_res)
            operators[opi] += 1


go(0, A[0])
print(ans_max, ans_min, sep='\n')
