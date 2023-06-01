from heapq import heappush, heappop


def solution(program):
    program.sort(key=lambda x: (x[1], x[0]), reverse=True)
    ans = [0] * 11
    ready_q = []
    cur = 0

    while ready_q or program:
        if not ready_q:
            heappush(ready_q, program.pop())
            cur = ready_q[0][1]
        a, b, c = heappop(ready_q)
        ans[a] += cur - b
        cur += c
        while program and program[-1][1] <= cur:
            heappush(ready_q, program.pop())
    ans[0] = cur
    return ans
