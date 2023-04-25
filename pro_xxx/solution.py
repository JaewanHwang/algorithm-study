def solution(ss):
    ans = []
    for s in ss:
        cur = 0
        last = -1
        s = list(s)
        while cur < len(s):
            if s[cur] == '1':
                if cur + 1 < len(s) and s[cur + 1] == '1' and last == -1:
                    last = cur
                cur += 1
            else:
                if last != -1:
                    l = max(0, cur - 2) - max(0, cur - 5)
                    s[cur - 2: cur + 1] = ['0'] * (3 - l) + s[max(0, cur - 5):  max(0, cur - 2)]
                    s[last: last + 3] = '110'
                    cur = last + 3
                    last = -1
                else:
                    cur += 1
        ans.append(''.join(s))
    return ans


print(solution(["1110", "100111100", "0111111010"]))
