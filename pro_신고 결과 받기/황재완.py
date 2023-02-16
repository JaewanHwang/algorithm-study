def solution(id_list, report, k):
    reported_dict = {uid: set() for uid in id_list}
    for r in report:
        reporter_id, reported_id = r.split()
        reported_dict[reported_id].add(reporter_id)
    ans = {uid: 0 for uid in id_list}
    for uid, reported_set in reported_dict.items():
        if len(reported_set) >= k:
            for reporter_id in reported_set:
                ans[reporter_id] += 1
    ans = list(ans.values())
    return ans
