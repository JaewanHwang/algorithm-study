def solution(enroll, referral, seller, amount):
    name2num = {name: i for i, name in enumerate(enroll)}
    name2num['-'] = -1
    referral = list(map(lambda x: name2num[x], referral))
    ans = [0] * len(enroll)

    for s, a in zip(seller, amount):
        cur_s = name2num[s]
        cur_b = a * 100
        while cur_s != -1:
            share = cur_b // 10
            ans[cur_s] += cur_b - share
            if share < 1:
                break
            cur_s = referral[cur_s]
            cur_b = share

    return ans
