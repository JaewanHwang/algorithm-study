def solution(queue1, queue2):
    tot_1 = sum(queue1)
    tot_2 = sum(queue2)
    target = (tot_1 + tot_2) // 2
    q = queue1 + queue2
    q1, q2 = 0, len(queue1)
    ans = -1
    t = 0
    history = set()
    while True:
        cur = (q1, q2) if q1 < q2 else (q2, q1)
        if cur in history:
            break
        history.add(cur)
        if tot_1 == tot_2:
            ans = t
            break
        elif tot_1 > tot_2:
            tot_1 -= q[q1]
            tot_2 += q[q1]
            q1 = (q1 + 1) % len(q)
        else:
            tot_2 -= q[q2]
            tot_1 += q[q2]
            q2 = (q2 + 1) % len(q)
        t += 1
    return ans
