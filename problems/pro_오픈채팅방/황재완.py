from collections import defaultdict


def solution(record):
    answer = []
    messages = []
    unht = defaultdict(str)
    for log in record:
        if log.startswith('Leave'):
            op, uid = log.split(' ')
        else:
            op, uid, nickname = log.split(' ')

        if op == 'Enter':
            messages.append((uid, '님이 들어왔습니다.'))
            unht[uid] = nickname
        elif op == 'Leave':
            messages.append((uid, '님이 나갔습니다.'))
        else:
            unht[uid] = nickname

    for uid, message in messages:
        answer.append(f'{unht[uid]}{message}')

    return answer