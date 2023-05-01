import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, H = map(int, input().split())
a = [0] * (H + 1)
for i in range(N):
    h = int(input())
    if i % 2 == 0:
        a[H] -= 1
        a[H - h] += 1
    else:
        a[h] -= 1
        a[0] += 1
s = [0] * (H + 1)
s[0] = a[0]
for i in range(1, H + 1):
    s[i] = s[i - 1] + a[i]
ans_1 = min(s[:H])
ans_2 = s[:H].count(ans_1)
print(ans_1, ans_2)
