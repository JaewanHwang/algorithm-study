import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
ans = 0
g, b = [[[False] * 4 for _ in range(6)] for _ in range(2)]
change_type = {1: 1, 2: 3, 3: 2}


def go(m, t, sy):
    global ans
    for x in range(2, 6):
        if ((t == 1 or t == 3) and m[x][sy]) or (t == 2 and (m[x][sy] or m[x][sy + 1])):
            x -= 1
            break
    m[x][sy] = True
    if t == 2:
        m[x][sy + 1] = True
    elif t == 3:
        m[x - 1][sy] = True

    break_cnt, break_x = 0, 0
    for x in range(5, 1, -1):
        if all(m[x]):
            break_cnt += 1
            break_x = x
            m[x] = [False] * 4

    ans += break_cnt

    if break_cnt > 0:
        m = [[False] * 4 for _ in range(break_cnt)] + m[:break_x] + m[break_x + break_cnt:]

    down_cnt = any(m[0]) + any(m[1])
    if down_cnt > 0:
        m = [[False] * 4 for _ in range(down_cnt)] + m[:6 - down_cnt]
    return m


for _ in range(N):
    t, x, y = map(int, input().split())
    g = go(g, t, y)
    b = go(b, change_type[t], x)

print(ans)
print(sum(sum(row) for row in g) + sum(sum(row) for row in b))
