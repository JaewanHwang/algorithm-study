import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
input = sys.stdin.readline

dice = list(map(int, input().split()))
piece_list = [0] * 4
m = [[i + 1, i + 1] for i in range(33)]
m[5][0] = 21
m[10][0] = 24
m[15][0] = 26
m[23] = [29, 29]
m[25] = [29, 29]
m[31] = [20, 20]
m[20] = [32, 32]
board = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 28, 27, 26,
         25, 30, 35, 0]


def go(n, tot):
    global ans
    if n == 10:
        ans = max(ans, tot)
        return
    for p in range(4):
        if piece_list[p] == 32:
            continue
        original_cur = piece_list[p]
        cur = m[original_cur][0]

        for _ in range(dice[n] - 1):
            if cur == 32:
                break
            cur = m[cur][1]
        fail = False
        for i in range(4):
            if piece_list[i] == cur != 32:
                fail = True
                break
        if not fail:
            piece_list[p] = cur
            go(n + 1, board[cur] + tot)
            piece_list[p] = original_cur


ans = 0
go(0, 0)
print(ans)
