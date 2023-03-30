from collections import Counter


def solution(str1, str2):
    set_a, set_b = Counter(), Counter()
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            set_a[str1[i:i + 2].upper()] += 1
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            set_b[str2[i:i + 2].upper()] += 1
    intersection_val, union_val = 0, 0
    for key in set(set_a.keys()) | set(set_b.keys()):
        intersection_val += min(set_a[key], set_b[key])
        union_val += max(set_a[key], set_b[key])
    return int((1 if intersection_val == union_val == 0 else intersection_val / union_val) * 65536)
