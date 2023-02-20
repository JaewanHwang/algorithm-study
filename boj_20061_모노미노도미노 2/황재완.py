import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

green_board = [[0] * 4 for _ in range(6)]
blue_board = [[0] * 4 for _ in range(6)]
ans = 0


def simulate(t, y, m):
    global ans

    if t == 1:
        for x in range(6):
            if m[x][y]:
                x -= 1
                break
        m[x][y] = 1
    elif t == 2:
        for x in range(6):
            if m[x][y] or m[x][y + 1]:
                x -= 1
                break
        m[x][y] = m[x][y + 1] = 1
    else:
        for x in range(6):
            if m[x][y]:
                x -= 1
                break
        m[x][y] = m[x - 1][y] = 1

    down_cnt, down_x = 0, 0
    for x in range(5, -1, -1):
        if all(m[x]):
            down_cnt += 1
            down_x = x
            m[x] = [0] * 4

    if down_cnt:
        for x in range(down_x - 1, -1, -1):
            m[x + down_cnt] = m[x]
        for x in range(down_cnt):
            m[x] = [0] * 4
        ans += down_cnt

    remove_cnt = 0
    for x in range(2):
        if any(m[x]):
            remove_cnt += 1
    if remove_cnt:
        for x in range(5 - remove_cnt, -1, -1):
            m[x + remove_cnt] = m[x]
        for x in range(remove_cnt):
            m[x] = [0] * 4


for _ in range(N):
    t, x, y = map(int, input().split())
    simulate(t, y, green_board)
    simulate(t if t == 1 else 5 - t, x, blue_board)

print(ans)
print(sum(map(sum, green_board)) + sum(map(sum, blue_board)))
