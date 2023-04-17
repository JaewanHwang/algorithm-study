import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
SIZE = 2 * N
belt = [[False, durability] for durability in map(int, input().split())]
s, e = 0, N - 1
cnt = 0
ans = 0
while cnt < K:
    s, e = (s - 1) % SIZE, (e - 1) % SIZE,
    if belt[e][0]:
        belt[e][0] = False
    for k in range(1, N - 1):
        i = (e - k) % SIZE
        ni = (i + 1) % SIZE
        if belt[i][0] and not belt[ni][0] and belt[ni][1] > 0:
            belt[ni][0], belt[i][0] = True, False
            belt[ni][1] -= 1
            if belt[ni][1] == 0:
                cnt += 1
    if belt[e][0]:
        belt[e][0] = False
    if belt[s][1] > 0:
        belt[s][1] -= 1
        belt[s][0] = True
        if belt[s][1] == 0:
            cnt += 1
    ans += 1
print(ans)
