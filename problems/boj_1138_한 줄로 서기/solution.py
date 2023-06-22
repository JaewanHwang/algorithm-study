import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
ans = [0] * N
for height, num in enumerate(a, start=1):
    cnt = 0
    for p in range(N):
        if ans[p] == 0:
            if cnt == num:
                ans[p] = height
                break
            cnt += 1

print(*ans)
