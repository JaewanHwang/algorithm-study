import sys

sys.stdin = open('input.txt')

m = [list(map(int, input().split())) for _ in range(10)]
counter = [5] * 6
CNT = 0
for x in range(10):
    for y in range(10):
        if m[x][y] == 1:
            CNT += 1


def ok(sx, sy, l):
    if sx + l > 10 or sy + l > 10:
        return False
    for x in range(sx, sx + l):
        for y in range(sy, sy + l):
            if m[x][y] == 0:
                return False
    return True


def go(i, n, rest):
    global ans
    if n >= ans:
        return
    if i == 100 or rest == 0:
        if rest == 0:
            ans = min(ans, n)
        return
    sx, sy = i // 10, i % 10
    if m[sx][sy] == 1:
        for l in range(1, 6):
            if counter[l] == 0:
                continue
            if not ok(sx, sy, l):
                break
            for x in range(sx, sx + l):
                for y in range(sy, sy + l):
                    m[x][y] = 0
            counter[l] -= 1
            go(i + 1, n + 1, rest - l * l)
            counter[l] += 1
            for x in range(sx, sx + l):
                for y in range(sy, sy + l):
                    m[x][y] = 1
    else:
        go(i + 1, n, rest)


ans = float('inf')
go(0, 0, CNT)
print(ans if ans != float('inf') else -1)
