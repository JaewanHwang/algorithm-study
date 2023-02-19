def ok(ans, m):
    for x, y, a in ans:
        if a == 0:  # 기둥 설치
            if not (y == 0 or any(m[x][y][1]) or m[x][y][0][1]):
                return False
        else:  # 보 설치
            if not (m[x][y][0][1] or m[x + 1][y][0][1] or (m[x][y][1][1] and m[x + 1][y][1][0])):
                return False
    return True


def solution(n, build_frame):
    m = [[[[False] * 2 for _ in range(2)] for _ in range(n + 1)] for _ in range(n + 1)]  # 0: 기둥, 1: 보
    ans = set()
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if a == 0:  # 기둥 설치
                if y == 0 or any(m[x][y][1]) or m[x][y][0][1]:
                    m[x][y][0][0] = m[x][y + 1][0][1] = True
                    ans.add((x, y, a))
            else:  # 보 설치
                if m[x][y][0][1] or m[x + 1][y][0][1] or (m[x][y][1][1] and m[x + 1][y][1][0]):
                    m[x][y][1][0] = m[x + 1][y][1][1] = True
                    ans.add((x, y, a))
        else:  # 삭제
            if a == 0:  # 기둥 삭제
                m[x][y][0][0] = m[x][y + 1][0][1] = False
            else:  # 보 삭제
                m[x][y][1][0] = m[x + 1][y][1][1] = False
            if not ok(ans, m):
                if a == 0:  # 기둥 삭제
                    m[x][y][0][0] = m[x][y + 1][0][1] = True
                else:  # 보 삭제
                    m[x][y][1][0] = m[x + 1][y][1][1] = True
            else:
                if (x, y, a) in ans:
                    ans.remove((x, y, a))

    return sorted(map(list, ans))
