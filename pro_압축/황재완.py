def solution(msg):
    ans = []
    dic = {chr(i + 65): i + 1 for i in range(26)}

    cur = 0
    while cur < len(msg):
        i = 0
        while cur + i < len(msg):
            if msg[cur: cur + i + 1] not in dic:
                dic[msg[cur: cur + i + 1]] = len(dic) + 1
                break
            i += 1
        ans.append(dic[msg[cur: cur + i]])
        cur += i

    return ans