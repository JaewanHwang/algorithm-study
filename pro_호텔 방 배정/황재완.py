import bisect


def solution(k, room_number):
    room_dict = dict()
    ans = []
    for request_num in room_number:
        if request_num not in room_dict:
            room_dict[request_num] = request_num + 1
        else:
            while request_num in room_dict:
                request_num = room_dict[request_num]
            room_dict[request_num] = request_num + 1
        ans.append(request_num)
    return ans
