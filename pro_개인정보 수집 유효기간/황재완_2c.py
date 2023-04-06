def solution(today, terms, privacies):
    term_map = dict()
    for term in terms:
        key, month = term.split()
        term_map[key] = 28 * int(month)
    today = int(today[:4]) * 28 * 12 + int(today[5:7]) * 28 + int(today[8:])
    ans = []
    for i, privacy in enumerate(privacies, start=1):
        date, term = privacy.split()
        date = int(date[:4]) * 28 * 12 + int(date[5:7]) * 28 + int(date[8:])
        if term_map[term] + date <= today:
            ans.append(i)
    return ans
