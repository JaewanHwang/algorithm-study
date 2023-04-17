import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
belt = [[a, False] for a in map(int, input().split())]
cnt = 0
ans = 0
while cnt < K:
    ans += 1
    belt = belt[-1:] + belt[:2 * N - 1]
    if belt[N - 1][1]:
        belt[N - 1][1] = False
    for i in range(N - 2, 0, - 1):
        if belt[i][1] and belt[i + 1][0] > 0 and not belt[i + 1][1]:
            belt[i][1], belt[i + 1][1], belt[i + 1][0] = False, True, belt[i + 1][0] - 1
            if belt[i + 1][0] == 0:
                cnt += 1
    if belt[N - 1][1]:
        belt[N - 1][1] = False
    if belt[0][0] > 0:
        belt[0][0] -= 1
        if belt[0][0] == 0:
            cnt += 1
        belt[0][1] = True

print(ans)
