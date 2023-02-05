# 풀이1
def solution(new_id):
    ans = ''
    # 1
    new_id = new_id.lower()
    # 2
    tmp = new_id
    new_id = ''
    for c in tmp:
        if c.isalpha() or c.isdigit() or c == '-' or c == '_' or c == '.':
            new_id += c
    # 3
    nnew_id = new_id.replace('..', '.')
    while nnew_id != new_id:
        new_id = nnew_id
        nnew_id = new_id.replace('..', '.')
    # 4
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:len(new_id) - 1]
    # 5
    if new_id == '':
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:len(new_id) - 1]
    # 7
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))

    ans = new_id
    return ans


# --------------------------------------------

# 풀이2
import re


def solution(new_id):
    ans = ''
    # 1
    new_id = new_id.lower()
    # 2
    tmp = new_id
    new_id = ''
    for c in tmp:
        if c.isalpha() or c.isdigit() or c == '-' or c == '_' or c == '.':
            new_id += c
    # 3
    p = re.compile('[.]{2,}')
    new_id = p.sub('.', new_id)
    # 4
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:len(new_id) - 1]
    # 5
    if new_id == '':
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:len(new_id) - 1]
    # 7
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))

    ans = new_id
    return ans

