def solution(msg):
    dictionary = {chr(64 + i): i for i in range(1, 27)}
    ans = []
    i = 0
    while i < len(msg):
        for j in range(i + 1, len(msg) + 1):
            if msg[i:j] not in dictionary:
                j -= 1
                break
        ans.append(dictionary[msg[i:j]])
        if j < len(msg):
            dictionary[msg[i:j + 1]] = len(dictionary) + 1
        i = j
    return ans
