# 풀이1
def solution(survey, choices):
    alpha_to_index = {'R': 0, 'T': 1, 'C': 2, 'F': 3, 'J': 4, 'M': 5, 'A': 6, 'N': 7}
    scores = [0] * 8

    for i, choice in enumerate(choices):
        scores[alpha_to_index[survey[i][choice // 4]]] += abs(choice - 4)

    scores = list(zip(scores, alpha_to_index.keys()))
    ans = ''
    for i in range(4):
        ans += min(scores[i * 2], scores[i * 2 + 1], key=lambda x: (-x[0], x[1]))[1]
    return ans

# 풀이2
def solution(survey, choices):
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i, choice in enumerate(choices):
        scores[survey[i][choice // 4]] += abs(choice - 4)

    scores = list(scores.items())
    ans = ''
    for i in range(4):
        ans += min(scores[i * 2], scores[i * 2 + 1], key=lambda x: (-x[1], x[0]))[0]
    return ans