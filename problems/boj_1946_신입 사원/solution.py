import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    a = [tuple(map(int, input().split())) for _ in range(N)]
    a.sort()
    min_y = float('inf')
    ans = 0
    for x, y in a:
        if y < min_y:
            ans += 1
            min_y = y
    print(ans)
