import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx = (-1, 0, 1)
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    if y - x == 1:
        print(1)
        continue

    print(ans)
