def solution(lottos, win_nums):
    win_nums = set(win_nums)
    cnt = 0
    change = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        if lotto == 0:
            change += 1

    return [7 - max(1, (cnt + change)), 7 - max(cnt, 1)]
