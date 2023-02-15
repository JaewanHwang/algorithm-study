from itertools import combinations


def solution(relation):
    R, C = len(relation), len(relation[0])
    candidate_keys = []
    for length in range(1, C + 1):
        for case in combinations(range(C), r=length):
            case = set(case)
            duplicate = False
            for candidate_key in candidate_keys:
                if candidate_key & case == candidate_key:
                    duplicate = True
                    break
            if duplicate:
                continue
            evaluate_set = set()
            for r in range(R):
                record = []
                for c in case:
                    record.append(relation[r][c])
                record = tuple(record)
                if record in evaluate_set:
                    break
                else:
                    evaluate_set.add(record)
            else:
                candidate_keys.append(case)

    ans = len(candidate_keys)
    return ans
