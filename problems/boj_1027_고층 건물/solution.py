import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    cnt = 0
    x1, y1 = i, arr[i]
    for l in range(i):
        x2, y2 = l, arr[l]
        ok = True
        for j in range(l + 1, i):
            if (y2 - y1) / (x2 - x1) * (j - x1) + y1 <= arr[j]:
                ok = False
                break
        if ok:
            cnt += 1

    for r in range(i + 1, N):
        x2, y2 = r, arr[r]
        ok = True
        for j in range(i + 1, r):
            if (y2 - y1) / (x2 - x1) * (j - x1) + y1 <= arr[j]:
                ok = False
                break
        if ok:
            cnt += 1

    ans = max(ans, cnt)
print(ans)
