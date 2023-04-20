import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
calendar = [[0] * 32 for _ in range(13)]
d, m, i = 1, 1, 0
while m < 13:
    calendar[m][d] = i
    i += 1
    if m in (4, 6, 9, 11):
        if d == 30:
            m += 1
            d = 1
            continue
    elif m == 2:
        if d == 28:
            m += 1
            d = 1
            continue
    else:
        if d == 31:
            m += 1
            d = 1
            continue
    d += 1

start, end = calendar[3][1], calendar[11][30]
arr = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    s = calendar[sm][sd]
    e = calendar[em][ed]
    arr.append((s, e))
arr.sort(reverse=True)
ans = 0
cur = start
max_e = 0
while arr:
    s, e = arr[-1]
    if cur < s:
        if max_e >= s:
            ans += 1
            cur = max_e
        else:
            break
    else:
        max_e = max(max_e, e)
        if max_e > end:
            ans += 1
            break
        arr.pop()

if max_e <= end:
    ans = 0
print(ans)
