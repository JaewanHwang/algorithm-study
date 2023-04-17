import sys

sys.setrecursionlimit(10 ** 6)


def go(max_min, s, e, d, num_list, op_list):
    if d[s][e][max_min] != -1:
        return d[s][e][max_min]
    if max_min == 0:
        d[s][e][0] = -float('inf')
        for op_i in range(s, e):
            if op_list[op_i] == '+':
                d[s][e][0] = max(d[s][e][0],
                                 go(0, s, op_i, d, num_list, op_list) + go(0, op_i + 1, e, d, num_list, op_list))
            elif op_list[op_i] == '-':
                d[s][e][0] = max(d[s][e][0],
                                 go(0, s, op_i, d, num_list, op_list) - go(1, op_i + 1, e, d, num_list, op_list))
    elif max_min == 1:
        d[s][e][1] = float('inf')
        for op_i in range(s, e):
            if op_list[op_i] == '+':
                d[s][e][1] = min(d[s][e][1],
                                 go(1, s, op_i, d, num_list, op_list) + go(1, op_i + 1, e, d, num_list, op_list))
            elif op_list[op_i] == '-':
                d[s][e][1] = min(d[s][e][1],
                                 go(1, s, op_i, d, num_list, op_list) - go(0, op_i + 1, e, d, num_list, op_list))

    return d[s][e][max_min]


def solution(arr):
    num_list = []
    op_list = []
    for i in range(len(arr)):
        if i % 2 == 0:
            num_list.append(int(arr[i]))
        else:
            op_list.append(arr[i])
    N = len(num_list)
    d = [[[-1] * 2 for _ in range(N)] for _ in range(N)]  # [최대값, 최소값]
    for i in range(N):
        d[i][i][0], d[i][i][1] = num_list[i], num_list[i]
    ans = go(0, 0, N - 1, d, num_list, op_list)
    return ans


print(solution(["1", "-", "8"]))
