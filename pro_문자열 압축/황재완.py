def solution(s):
    ans = len(s)
    for cut_length in range(1, len(s) // 2 + 1):
        res = ''
        cnt = 1
        last = s[:cut_length]
        for i in range(cut_length, len(s), cut_length):
            cur = s[i:i + cut_length]
            if cur != last:
                res += (str(cnt) if cnt > 1 else '') + last
                last = cur
                cnt = 1
            else:
                cnt += 1
        res += (str(cnt) if cnt > 1 else '') + cur
        ans = min(ans, len(res))
    return ans
