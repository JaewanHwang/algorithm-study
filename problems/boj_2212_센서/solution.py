import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
K = int(input())
a = sorted(set(map(int, input().split())))
s = [0] * (len(a) - 1)
for i in range(1, len(a)):
    s[i - 1] = a[i] - a[i - 1]
s.sort()
k = 0
while s and k < K - 1:
    s.pop()
    k += 1
ans = sum(s)
print(ans)
