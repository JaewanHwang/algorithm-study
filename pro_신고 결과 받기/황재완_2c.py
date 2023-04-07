from collections import defaultdict


def solution(id_list, report, k):
    report_set = set(report)
    counter = defaultdict(list)
    for record in report_set:
        reporter, reported = record.split(' ')
        counter[reported].append(reporter)
    email = defaultdict(int)
    for key, val in counter.items():
        if len(val) >= k:
            for reporter in val:
                email[reporter] += 1
    ans = []
    for id in id_list:
        ans.append(email[id])
    return ans
