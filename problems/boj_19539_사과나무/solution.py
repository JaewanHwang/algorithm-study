import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
h = list(map(int, input().split()))
d, m = divmod(sum(h), 3)
if m != 0:
    print('NO')
else:
    cnt = 0
    for cur in h:
        cnt += cur // 2
    if cnt >= d:
        print('YES')
    else:
        print('NO')
