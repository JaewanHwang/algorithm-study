# 풀이 1, while문 사용
def solution(s):
    word2digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    ans = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            ans += s[i]
            i += 1
        else:
            for j in range(3, 6):
                if s[i: i + j] in word2digit:
                    ans += word2digit[s[i:i + j]]
                    i += j
                    break
    return int(ans)


# 풀이 2, replace 사용
def solution(s):
    word2digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    ans = s
    for key, val in word2digit.items():
        ans = ans.replace(key, val)
    return int(ans)
