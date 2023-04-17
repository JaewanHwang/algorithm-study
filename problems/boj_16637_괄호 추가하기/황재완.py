import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(input())
exp = list(input())
operators = []
operands = []
for i in range(0, len(exp), 2):
    operands.append(int(exp[i]))
    if i + 1 < len(exp):
        operators.append(exp[i + 1])


def calculate():
    global ans
    q = deque()
    i = 0
    while i < len(operands):
        if (i < len(operators) and not used[i]) or i == len(operators):
            q.append(operands[i])
            if i < len(operators):
                q.append(operators[i])
            i += 1
        else:
            op1 = operands[i]
            op2 = operands[i + 1]
            op = operators[i]
            if op == '+':
                res = op1 + op2
            elif op == '-':
                res = op1 - op2
            else:
                res = op1 * op2
            q.append(res)
            if i + 1 < len(operators):
                q.append(operators[i + 1])
            i += 2
    stack = []
    while q:
        cur = q.popleft()
        if cur not in ('+', '-', '*') and stack:
            operator = stack.pop()
            operand = stack.pop()
            if operator == '+':
                res = operand + cur
            elif operator == '-':
                res = operand - cur
            else:
                res = operand * cur
            stack.append(res)
        else:
            stack.append(cur)
    ans = max(ans, stack.pop())


def go(i):
    if i == len(operands):
        calculate()
        return
    # 괄호를 추가하지 않음
    go(i + 1)
    # 괄호를 추가함
    if (0 < i < len(operators) and not used[i - 1]) or (i == 0 and i < len(operators)):
        used[i] = True
        go(i + 2)
        used[i] = False


ans = -float('inf')
used = [False] * len(operators)
go(0)
print(ans)
