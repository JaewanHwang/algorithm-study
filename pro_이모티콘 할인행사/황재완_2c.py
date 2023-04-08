from itertools import product


def solution(users, emoticons):
    ans = []
    for case in product((10, 20, 30, 40), repeat=len(emoticons)):
        res = [0, 0]
        for discount_rate, threshold in users:
            tot = sum(map(lambda x: emoticons[x] * (100 - case[x]) / 100,
                          filter(lambda x: case[x] >= discount_rate, range(len(emoticons)))))
            if tot >= threshold:
                res[0] += 1
            else:
                res[1] += tot
        ans.append(res)
    ans = max(ans)
    return ans
