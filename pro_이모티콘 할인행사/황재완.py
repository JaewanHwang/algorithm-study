def go(n, users, emoticons):
    if n == len(emoticons):
        evaluate(users, emoticons)
        return
    for discount in (10, 20, 30, 40):
        discounts[n] = discount
        go(n + 1, users, emoticons)


def evaluate(users, emoticons):
    global ans
    res = [0, 0]
    for threshold_discount, threshold_price in users:
        total_price = 0
        for i, emoticon in enumerate(emoticons):
            if threshold_discount <= discounts[i]:
                total_price += emoticon * (100 - discounts[i]) // 100
        if total_price >= threshold_price:
            res[0] += 1
        else:
            res[1] += total_price
    if ans[0] < res[0]:
        ans = res
    elif ans[0] == res[0] and ans[1] < res[1]:
        ans = res


discounts = None
ans = [0, 0]


def solution(users, emoticons):
    global discounts
    discounts = [0] * len(emoticons)
    go(0, users, emoticons)
    return ans
