def construct(x, y, a, pillar, plane, m):
    m[x][y][a] = True
    if a == 0:
        pillar.add((x, y))
    else:
        plane.add((x, y))

    if not check(pillar, plane, m):
        m[x][y][a] = False
        if a == 0:
            pillar.remove((x, y))
        else:
            plane.remove((x, y))


def remove(x, y, a, pillar, plane, m):
    m[x][y][a] = False
    if a == 0:
        pillar.remove((x, y))
    else:
        plane.remove((x, y))

    if not check(pillar, plane, m):
        m[x][y][a] = True
        if a == 0:
            pillar.add((x, y))
        else:
            plane.add((x, y))


def check(pillar, plane, m):
    for x, y in pillar:
        if y == 0 or m[x][y][1] or m[x - 1][y][1] or m[x][y - 1][0]:
            continue
        else:
            return False

    for x, y in plane:
        if m[x][y - 1][0] or m[x + 1][y - 1][0] or (m[x - 1][y][1] and m[x + 1][y][1]):
            continue
        else:
            return False
    return True


def solution(n, build_frame):
    pillar = set()
    plane = set()
    m = [[[False] * 2 for _ in range(n + 1)] for _ in range(n + 1)]

    for x, y, a, b in build_frame:
        if b == 1:
            construct(x, y, a, pillar, plane, m)
        else:
            remove(x, y, a, pillar, plane, m)
    ans = []
    for x, y in pillar:
        ans.append([x, y, 0])
    for x, y in plane:
        ans.append([x, y, 1])
    ans.sort()
    return ans


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
