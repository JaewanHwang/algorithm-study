def solution(today, terms, privacies):
    Y, m, d = map(int, today.split('.'))
    today = Y * 12 * 28 + m * 28 + d
    terms_dict = dict()
    for term in terms:
        term_name, term_month = term.split(' ')
        terms_dict[term_name] = int(term_month) * 28
    ans = []
    for i, privacy in enumerate(privacies, start=1):
        Ymd, term_name = privacy.split(' ')
        Y, m, d = map(int, Ymd.split('.'))
        get_day = Y * 12 * 28 + m * 28 + d
        if today - get_day >= terms_dict[term_name]:
            ans.append(i)
    return ans