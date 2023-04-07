import sys

sys.setrecursionlimit(10 ** 6)


def go(cur, room):
    if cur not in room:
        return cur
    res = go(room[cur], room)
    room[cur] = res
    return res


def solution(k, room_number):
    room = dict()
    ans = []
    for num in room_number:
        if num not in room:
            ans.append(num)
            room[num] = num + 1
        else:
            next = go(num, room)
            ans.append(next)
            room[next] = next + 1
    return ans
