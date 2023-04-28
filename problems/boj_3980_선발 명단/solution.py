import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def go(i, now):
    global ans
    if i == 11:
        ans = max(ans, now)
        return
    for pos in range(11):
        if m[i][pos] == 0 or occupied[pos]:
            continue
        occupied[pos] = True
        go(i + 1, m[i][pos] + now)
        occupied[pos] = False


C = int(input())
for _ in range(C):
    ans = 0
    occupied = [False] * 11
    m = [list(map(int, input().split())) for _ in range(11)]
    go(0, 0)

    print(ans)
