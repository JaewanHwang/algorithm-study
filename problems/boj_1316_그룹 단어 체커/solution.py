import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
ans = N
for _ in range(N):
    history = dict()
    s = input().rstrip()
    for i, char in enumerate(s):
        if char in history and i - history[char] > 1:
            ans -= 1
            break
        history[char] = i
print(ans)
