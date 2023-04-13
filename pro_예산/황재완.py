from itertools import accumulate


def solution(d, budget):
    for i, tot in enumerate(accumulate(sorted(d))):
        if tot > budget:
            return i
        elif tot == budget:
            return i + 1
    return i + 1
