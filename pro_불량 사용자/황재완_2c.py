import re
from itertools import permutations


def solution(user_id, banned_id):
    ans = set()
    banned_id_len = [0] * len(banned_id)
    for i in range(len(banned_id)):
        banned_id_len[i] = len(banned_id[i])
        banned_id[i] = banned_id[i].replace('*', '[a-z0-9]')
    for case in permutations(user_id, r=len(banned_id)):
        for blen, bid, uid in zip(banned_id_len, banned_id, case):
            if blen != len(uid) or not re.match(bid, uid):
                break
        else:
            ans.add(tuple(sorted(case)))
    return len(ans)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
