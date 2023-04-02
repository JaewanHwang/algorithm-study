from itertools import combinations


def solution(orders, course):
    all_menus = set()
    for i, order in enumerate(orders):
        orders[i] = set(order)
        all_menus |= orders[i]
    ans = []
    for l in course:
        candidates = []
        for case in combinations(all_menus, r=l):
            cnt = 0
            menu = set(case)
            for order in orders:
                if menu <= order:
                    cnt += 1
            if cnt >= 2:
                candidates.append((cnt, ''.join(sorted(menu))))
        candidates.sort(reverse=True)
        for cnt, menu in candidates:
            if cnt == candidates[0][0]:
                ans.append(menu)
            else:
                break
    return sorted(ans)
