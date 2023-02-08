# 풀이1
from functools import reduce

ans = set()
dictionary = None
used = None


def go(i, word, uid):
    if i == len(uid):
        dictionary[uid].add(word)
        return
    go(i + 1, word + uid[i], uid)
    go(i + 1, word + '*', uid)


def go2(i, banned_id):
    if i == len(banned_id):
        ans.add(reduce(lambda x, y: 10 * x + used[y], used, 0))
        return
    for uid in dictionary:
        if banned_id[i] in dictionary[uid] and not used[uid]:
            used[uid] = 1
            go2(i + 1, banned_id)
            used[uid] = 0


def solution(user_id, banned_id):
    global dictionary, used
    used = {uid: 0 for uid in user_id}
    dictionary = {uid: set() for uid in user_id}
    for uid in dictionary:
        go(0, '', uid)
    go2(0, banned_id)
    return len(ans)


# --------------------------------------------------
# 풀이2
'''
permutations와 re를 이용한 간단 풀이
'''
from itertools import permutations
import re


def solution(user_id, banned_id):
    ans = set()
    for i, bid in enumerate(banned_id):
        banned_id[i] = bid.replace('*', '.')
    print(banned_id)
    for perm in permutations(range(len(user_id)), r=len(banned_id)):
        for i, uid in enumerate(perm):
            if len(banned_id[i]) != len(user_id[uid]) or not re.match(banned_id[i], user_id[uid]):
                break
        else:
            ans.add(tuple(sorted(perm)))
    print(ans)
    return len(ans)
