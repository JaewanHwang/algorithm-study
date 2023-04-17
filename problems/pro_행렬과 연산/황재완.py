from collections import deque


def solution(rc, operations):
    R, C = len(rc), len(rc[0])
    mat = rc
    first = deque(mat[0][:])
    last = deque(mat[-1][:])
    left = deque(mat[r][0] for r in range(R - 2, 0, -1))
    right = deque(mat[r][-1] for r in range(1, R - 1, 1))
    mid = deque(deque(mat[r][1: C - 1]) for r in range(1, R - 1, 1))
    for operation in operations:
        if operation == 'ShiftRow':
            right.appendleft(first.pop())
            left.append(first.popleft())
            mid.appendleft(first)
            first = last
            last = mid.pop()
            last.appendleft(left.popleft())
            last.append(right.pop())
        else:
            right.appendleft(first.pop())
            last.append(right.pop())
            left.appendleft(last.popleft())
            first.appendleft(left.pop())
    ans = [list(first)]
    while mid:
        ans.append([left.pop()] + list(mid.popleft()) + [right.popleft()])
    ans.append(list(last))
    return ans


print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
