from itertools import permutations
from collections import deque


def solution(expression):
    original_exp = deque()
    last = ''
    op_set = set()
    for c in expression:
        if c.isdigit():
            last += c
        else:
            op_set.add(c)
            original_exp.append(last)
            original_exp.append(c)
            last = ''
    original_exp.append(last)
    ans = 0
    for priority in permutations(op_set):
        exp = deque(original_exp)
        for op in priority:
            new_exp = deque()
            while exp:
                token = exp.popleft()
                if token not in op_set and new_exp and new_exp[-1] == op:
                    new_exp.pop()
                    new_exp.append(str(eval(new_exp.pop() + op + token)))
                else:
                    new_exp.append(token)
            exp = new_exp
        ans = max(ans, abs(int(exp.pop())))
    return ans
