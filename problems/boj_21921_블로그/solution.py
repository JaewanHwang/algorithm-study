import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, X = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + a[i - 1]
ans = 0
cnt = 0
for e in range(X, N + 1):
    hit = s[e] - s[e - X]
    if hit > ans:
        ans = hit
        cnt = 1
    elif ans == hit:
        cnt += 1
if ans == 0:
    print('SAD')
else:
    print(ans, cnt, sep='\n')
