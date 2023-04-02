import re


def solution(files):
    ans = []
    for i, file in enumerate(files):
        result = re.search(r'(\D+)(\d{1,5})', file)
        ans.append((result.group(1).upper(), int(result.group(2)), i, file))
    ans.sort()
    ans = list(file for _, _, _, file in ans)
    return ans
