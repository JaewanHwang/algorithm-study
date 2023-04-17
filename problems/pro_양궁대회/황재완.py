# 아예 0개를 써서 지거나 이길거면 +1개만큼 더쏴서 이기는 방법으로 모든 경우의 수를 구하고 ans값 갱신, 만약 n발 다 못쐈으면 0점에 나머지를 모두 맞춘다.

ans_diff, ans_min, N, apeach_info = 0, None, 0, None

def go(i, cnt, ryan_info, score_ryan, score_apeach):
    global ans_diff, ans_min
    if i == 11:
        if cnt > 0:
            ryan_info[10] += cnt
        diff = score_ryan - score_apeach
        if diff == 0:
            return
        if ans_diff < diff:
            ans_diff, ans_min = diff, ryan_info[:]
        elif ans_diff == diff:
            for j in range(10, -1, -1):
                if ryan_info[j] > ans_min[j]:
                    ans_min = ryan_info[:]
                    break
                elif ryan_info[j] < ans_min[j]:
                    break

        ryan_info[10] -= cnt
        return

    ryan_info[i] = 0
    go(i + 1, cnt, ryan_info, score_ryan, score_apeach + (10 - i if apeach_info[i] >= 1 else 0))
    if apeach_info[i] < cnt:
        ryan_info[i] = apeach_info[i] + 1
        go(i + 1, cnt - ryan_info[i], ryan_info, score_ryan + (10 - i), score_apeach)
        ryan_info[i] = 0


def solution(n, info):
    global N, apeach_info
    N, apeach_info = n, info
    go(0, N, [0] * 11, 0, 0)
    if ans_diff > 0:
        return ans_min
    return [-1]