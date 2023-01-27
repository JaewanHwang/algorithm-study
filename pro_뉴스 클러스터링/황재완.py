from collections import Counter

def get_set(str):
    s = Counter()
    for i in range(len(str) - 1):
        token = str[i: i + 2]
        if not token.isalpha():
            continue
        s[token] += 1
    return s


def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    s1 = get_set(str1)
    s2 = get_set(str2)
    ans = int((sum((s1 & s2).values()) / sum((s1 | s2).values()) if sum((s1 | s2).values()) != 0 else 1) * 65536)
    return ans
