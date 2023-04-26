import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
last1 = list(map(int, input().split()))
last2 = list(last1)
dp1, dp2 = [0] * 3, [0] * 3
for _ in range(N - 1):
    m = list(map(int, input().split()))
    dp1[0] = max(last1[0], last1[1]) + m[0]
    dp1[1] = max(last1) + m[1]
    dp1[2] = max(last1[1], last1[2]) + m[2]

    dp2[0] = min(last2[0], last2[1]) + m[0]
    dp2[1] = min(last2) + m[1]
    dp2[2] = min(last2[1], last2[2]) + m[2]

    tmp1, tmp2 = last1, last2
    last1, last2 = dp1, dp2
    dp1, dp2 = tmp1, tmp2

print(max(last1), min(last2))
