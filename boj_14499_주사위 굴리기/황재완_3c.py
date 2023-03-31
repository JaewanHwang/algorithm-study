import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

operations = list(map(int, input().split()))
pieces = [0] * 4
m = [[i + 1, i + 1, i * 2] for i in range(19)]
m += [0] * 14
m[19] = [31, 31, 38]
m[5] = [6, 20, 10]
m[20] = [21, 21, 13]
m[21] = [22, 22, 16]
m[22] = [28, 28, 19]
m[10] = [11, 23, 20]
m[23] = [24, 24, 22]
m[24] = [28, 28, 24]
m[15] = [16, 25, 30]
m[25] = [26, 26, 28]
m[26] = [27, 27, 27]
m[27] = [28, 28, 26]
m[28] = [29, 29, 25]
m[29] = [30, 30, 30]
m[30] = [31, 31, 35]
m[31] = [32, 32, 40]
m[32] = [-1, -1, 0]


def go(i, tot):
    if i == 10:
        return tot
    res = 0
    for pi in range(4):
        if pieces[pi] == len(m) - 1:
            continue
        cur = m[pieces[pi]][1]
        for _ in range(operations[i] - 1):
            if cur == len(m) - 1:
                break
            cur = m[cur][0]
        failed = False
        for position in pieces:
            if cur == position != len(m) - 1:
                failed = True
                break
        if failed:
            continue

        original_position = pieces[pi]
        pieces[pi] = cur
        res = max(res, go(i + 1, tot + m[cur][2]))
        pieces[pi] = original_position
    return res


ans = go(0, 0)
print(ans)
