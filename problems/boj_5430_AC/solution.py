import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    a = input().rstrip()[1:-1].split(',')
    if n == 0:
        if 'D' in p:
            print('error')
        else:
            print('[]')
        continue

    ptr = [0, n - 1]
    cur = 0
    for op in p:
        if op == 'R':
            cur = 1 - cur
        else:
            if ptr[0] > ptr[1]:
                print('error')
                break
            if cur == 0:
                ptr[cur] += 1
            else:
                ptr[cur] -= 1
    else:
        ans = a[ptr[0]:ptr[1] + 1]
        print(f'[{",".join(ans if cur == 0 else ans[::-1])}]')
