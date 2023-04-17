def solution(s):
    superset = []
    s = s[1:len(s) - 1].replace('},', '}.')
    for subset in s.split('.'):
        superset.append(set(map(int, subset[1:len(subset) - 1].split(','))))
    superset.sort(key=lambda x: len(x))
    ans = []
    curset = set()
    for subset in superset:
        ans.append(*(subset - curset))
        curset = subset
    return ans
