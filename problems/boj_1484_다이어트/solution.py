import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

G = int(input())
l, r = 1, 1
ans = set()
while l <= G and r <= G:
    cur = r * r - l * l
    if cur == G:
        ans.add(r)
        r += 1
    elif cur > G:
        l += 1
    else:
        r += 1
if ans:
    print(*sorted(ans), sep='\n')
else:
    print(-1)
