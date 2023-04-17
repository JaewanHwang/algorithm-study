# 풀이1 -> 정확성 테스트만 통과
from collections import defaultdict


def solution(info, query):
    filter_sets = [defaultdict(set) for _ in range(4)]
    scores = [0] * len(info)
    for num, a_info in enumerate(info):
        a_info = a_info.split(' ')
        for i in range(4):
            filter_sets[i][a_info[i]].add(num)
        scores[num] = int(a_info[-1])

    ans = [0] * len(query)
    super_set = set(range(len(info)))
    for qi, q in enumerate(query):
        cur = super_set
        q = q.replace(' and ', ' ').split(' ')
        score = int(q[-1])
        for i in range(len(q) - 1):
            if q[i] == '-':
                continue
            cur = cur & filter_sets[i][q[i]]
        for c in cur:
            if scores[c] >= score:
                ans[qi] += 1
    return ans


# 풀이2 -> 효율성 테스트도 모두 통과
import bisect


def solution(info, query):
    all_combinations = [[[[[0] * 4] for _ in range(3)] for _ in range(3)] for _ in range(3)]
    all_combinations = {language: {
        position: {career: {soulfood: [] for soulfood in ('chicken', 'pizza', '-')} for career in
                   ('junior', 'senior', '-')} for position in ('backend', 'frontend', '-')} for language in
        ('cpp', 'java', 'python', '-')}
    for a_info in info:
        language, position, career, soulfood, score = a_info.split(' ')
        for l in (language, '-'):
            for p in (position, '-'):
                for c in (career, '-'):
                    for s in (soulfood, '-'):
                        all_combinations[l][p][c][s].append(int(score))

    for l in ('cpp', 'java', 'python', '-'):
        for p in ('backend', 'frontend', '-'):
            for c in ('junior', 'senior', '-'):
                for s in ('chicken', 'pizza', '-'):
                    all_combinations[l][p][c][s].sort()

    ans = [0] * len(query)
    for qi, q in enumerate(query):
        l, p, c, last = q.split(' and ')
        s, score = last.split(' ')
        ans[qi] += len(all_combinations[l][p][c][s]) - bisect.bisect_left(all_combinations[l][p][c][s], int(score))

    return ans
