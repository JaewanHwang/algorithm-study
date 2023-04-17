def solution(s):
    ans = len(s)
    for l in range(1, len(s) // 2 + 1):
        res = ''
        last, cnt = '', 0
        for i in range(0, len(s), l):
            if s[i: i + l] == last:
                cnt += 1
            else:
                res += (str(cnt) if cnt >= 2 else '') + last
                last = s[i:i + l]
                cnt = 1
        res += (str(cnt) if cnt >= 2 else '') + last
        ans = min(ans, len(res))
    return ans
