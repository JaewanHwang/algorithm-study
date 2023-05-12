import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
m = [[0] * (N + 1) for _ in range(366)]
schedule = [list(map(int, input().split())) for _ in range(N)]
schedule.sort(key=lambda x: (x[0], -x[1]))
height = [0] * 366
for s, e in schedule:
    for i in range(N + 1):
        if m[s][i] == 0:
            break
    for d in range(s, e + 1):
        m[d][i] = 1
        height[d] = max(height[d], i + 1)
ans = 0
l, h = 0, 0
for d in range(1, 366):
    if height[d] >= 1:
        l += 1
        h = max(height[d], h)
    else:
        ans += l * h
        l, h = 0, 0
ans += l * h
print(ans)
