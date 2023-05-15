import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())
s = 2
ans = ''
for d in bin(s + (K - 1))[3:]:
    if d == '0':
        ans += '4'
    else:
        ans += '7'
print(ans)
