import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
nums = []

A, B = map(int, input().split())


def go(i, cur):
    if i == cnt:
        nums.append(cur)
        return
    go(i + 1, 10 * cur + 4)
    go(i + 1, 10 * cur + 7)


for cnt in range(1, 10):
    go(0, 0)

ans = 0
for num in nums:
    if A <= num <= B:
        ans += 1
    elif num > B:
        break
print(ans)
