def solution(records):
    uid2nickname = {}
    for record in records:
        op, *uid_nickname = record.split()
        if len(uid_nickname) >= 2:
            uid, nickname = uid_nickname
            uid2nickname[uid] = nickname
    ans = []
    for record in records:
        op, *uid_nickname = record.split()
        if op == 'Enter':
            uid, _ = uid_nickname
            ans.append(f'{uid2nickname[uid]}님이 들어왔습니다.')
        elif op == 'Leave':
            uid = uid_nickname[0]
            ans.append(f'{uid2nickname[uid]}님이 나갔습니다.')

    return ans
