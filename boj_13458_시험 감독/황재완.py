import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
A = map(int, input().split())
B, C = map(int, input().split())
ans = 0


for Ai in A:
    ans += 1
    if Ai <= B:
        continue
    else:
        rest = Ai - B
        div = rest // C
        if rest % C == 0:
            ans += div
        else:
            ans += div + 1

print(ans)