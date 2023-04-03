from collections import Counter


def solution(gems):
    all_gems = set(gems)
    counter = Counter()
    l, r = 0, 0
    counter[gems[0]] += 1
    ans = []
    while l <= r < len(gems):
        if len(counter) == len(all_gems):
            ans.append((l + 1, r + 1))
            counter[gems[l]] -= 1
            if counter[gems[l]] == 0:
                counter.pop(gems[l])
            l += 1
        else:
            r += 1
            if r < len(gems):
                counter[gems[r]] += 1
    ans = min(ans, key=lambda x: (x[1] - x[0], x[0]))
    return ans


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
