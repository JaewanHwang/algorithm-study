def go(i, start, s, course, orders, all_menus):
    if i in course:
        cnt = 0
        for order in orders:
            if s <= order:
                cnt += 1
        if cnt >= 2:
            candidates[i].append((cnt, ''.join(sorted(s))))
        else:
            return
    for j in range(start, len(all_menus)):
        s.add(all_menus[j])
        go(i + 1, j + 1, s, course, orders, all_menus)
        s.remove(all_menus[j])


candidates = [[] for _ in range(11)]


def solution(orders, course):
    all_menus = set()
    for i, order in enumerate(orders):
        all_menus |= set(orders[i])
        orders[i] = set(order)
    go(0, 0, set(), set(course), orders, sorted(all_menus))
    ans = []
    for l in course:
        candidates[l].sort(reverse=True)
        for cnt, s in candidates[l]:
            if cnt == candidates[l][0][0]:
                ans.append(s)
            else:
                break
    return sorted(ans)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
