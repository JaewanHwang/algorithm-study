import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
open = list(map(int, input().split()))
M = int(input())
arr = [int(input()) for _ in range(M)]
ans = float('inf')


def go(i, cnt, open):
    global ans
    if i == M:
        ans = min(ans, cnt)
        return
    now = arr[i]
    if now in open:
        go(i + 1, cnt, open)
    else:
        go(i + 1, cnt + abs(open[0] - now), [now, open[1]])

        go(i + 1, cnt + abs(open[1] - now), [open[0], now])


go(0, 0, open)
print(ans)
