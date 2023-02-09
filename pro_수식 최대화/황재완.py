import re
from itertools import permutations
from collections import deque
def solution(expression):
    nums = re.split('[*+-]', expression)
    ops = re.findall('[*+-]', expression)
    Q = deque()
    for i in range(len(nums) - 1):
        Q.append(nums[i])
        Q.append(ops[i])
    Q.append(nums[-1])
    ops_kinds = set(ops)
    ans = 0
    for priority in permutations(ops_kinds):
        exp = Q
        for op in priority:
            i = 0
            nexp = []
            while i < len(exp):
                if exp[i].isdigit() or exp[i] != op:
                    nexp.append(exp[i])
                else:
                    op1 = nexp.pop()
                    i += 1
                    op2 = exp[i]
                    nexp.append(str(eval(op1 + op + op2)))
                i += 1
            exp = nexp
        ans = max(ans, abs(int(exp.pop())))
    return ans