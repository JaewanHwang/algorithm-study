import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for i in range(N):
    ans += 1

    remain = A[i] - B
    if remain <= 0:
        continue
    ans += remain // C + (1 if remain % C > 0 else 0)
print(ans)
