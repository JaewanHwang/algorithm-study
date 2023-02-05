# 풀이1
from collections import deque

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def get_dist(f, number):
    d = [[-1] * 3 for _ in range(4)]
    q = deque([f])
    d[f[0]][f[1]] = 0
    while q:
        x, y = q.popleft()
        if keypad[x][y] == number:
            return x, y, d[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 3 and d[nx][ny] == -1:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1


def solution(numbers, hand):
    answer = ''
    lf, rf = [3, 0], [3, 2]
    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            lf = [(number - 1) // 3, (number - 1) % 3]
        elif number in (3, 6, 9):
            answer += 'R'
            rf = [(number - 1) // 3, (number - 1) % 3]
        else:
            lx, ly, ld = get_dist(lf, number)
            rx, ry, rd = get_dist(rf, number)
            if ld < rd or (ld == rd and hand == 'left'):
                lf = [lx, ly]
                answer += 'L'
            elif ld > rd or (ld == rd and hand == 'right'):
                rf = [rx, ry]
                answer += 'R'

    return answer
# -----------------------------------------------------------------
# 풀이 2
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]


def get_dist(f, number):
    tx, ty = ((number - 1) // 3, (number - 1) % 3) if number != 0 else (3, 1)
    sx, sy = f
    return abs(tx - sx) + abs(ty - sy)


def solution(numbers, hand):
    answer = ''
    lf, rf = [3, 0], [3, 2]
    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            lf = [(number - 1) // 3, (number - 1) % 3]
        elif number in (3, 6, 9):
            answer += 'R'
            rf = [(number - 1) // 3, (number - 1) % 3]
        else:
            ld = get_dist(lf, number)
            rd = get_dist(rf, number)

            if ld < rd or (ld == rd and hand == 'left'):
                lf = ((number - 1) // 3, (number - 1) % 3) if number != 0 else (3, 1)
                answer += 'L'
            elif ld > rd or (ld == rd and hand == 'right'):
                rf = ((number - 1) // 3, (number - 1) % 3) if number != 0 else (3, 1)
                answer += 'R'

    return answer
