import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def go(i):
    if i >= N:
        return 0
    if d[i] != -1:
        return d[i]
    d[i] = go(i + 1)
    time, reward = time_reward[i]
    if i + time <= N:
        d[i] = max(d[i], go(i + time) + reward)
    return d[i]


N = int(input())
time_reward = [tuple(map(int, input().split())) for _ in range(N)]
d = [-1] * N
ans = go(0)
print(ans)
