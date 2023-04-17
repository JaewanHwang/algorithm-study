import sys

sys.setrecursionlimit(10 ** 6)


def go(num, room_dict):
    if num not in room_dict:
        room_dict[num] = num + 1
        return num
    room_dict[num] = go(room_dict[num], room_dict)
    return room_dict[num]


def solution(k, room_number):
    ans = [0] * len(room_number)
    room_dict = dict()
    for i, num in enumerate(room_number):
        ans[i] = go(num, room_dict)
    return ans


print(solution(10, [1, 3, 4, 1, 3, 1]))
