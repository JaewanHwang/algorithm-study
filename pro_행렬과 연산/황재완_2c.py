from collections import deque


def solution(rc, operations):
    N, M = len(rc), len(rc[0])
    left, right, middle = (deque() for _ in range(3))
    for x in range(N):
        left.append(rc[N - 1 - x][0])
        right.append(rc[x][M - 1])
        middle.append(deque(rc[x][1:M - 1]))
    for op in operations:
        if op == 'Rotate':
            top, bottom = middle[0], middle[-1]
            cur = left.pop()
            top.appendleft(cur)
            cur = top.pop()
            right.appendleft(cur)
            cur = right.pop()
            bottom.append(cur)
            cur = bottom.popleft()
            left.appendleft(cur)
        else:
            middle.rotate(1)
            left.rotate(-1)
            right.rotate(1)
        ans = []
    for x in range(N):
        ans.append([left.pop()] + list(middle.popleft()) + [right.popleft()])
    return ans
