import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
N, K = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(1, N):
    b.append((a[i] - a[i - 1]))
b.sort(reverse=True)
ans = sum(b) - sum(b[:K - 1])
print(ans)
