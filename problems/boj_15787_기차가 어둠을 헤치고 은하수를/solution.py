import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
trains = [deque([False] * 20, maxlen=20) for _ in range(N)]
for _ in range(M):
    op, *ix = map(int, input().split())
    ix[0] -= 1
    if op == 1:
        i, x = ix
        x -= 1
        trains[i][x] = True
    elif op == 2:
        i, x = ix
        x -= 1
        trains[i][x] = False
    elif op == 3:
        i, = ix
        trains[i].appendleft(False)
    else:
        i, = ix
        trains[i].append(False)

states = set()
for train in trains:
    state = 0
    for occupied in train:
        state *= 10
        if occupied:
            state += 1
    states.add(state)
ans = len(states)
print(ans)
