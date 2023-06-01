import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

if sum(budget) <= M:
    print(max(budget))
    sys.exit(0)

l, r = 0, max(budget)
while l <= r:
    mid = (l + r) // 2
    tot = 0
    for b in budget:
        if b <= mid:
            tot += b
        else:
            tot += mid
    if tot <= M:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)
