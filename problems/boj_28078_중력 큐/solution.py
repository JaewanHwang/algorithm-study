import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

Q = int(input())
q = deque()
direction = 0  # 뒤 - 앞: 0, 뒤 | 앞: 1, 앞 - 뒤: 2, 앞 | 뒤: 3
cnt = [0, 0]  # 0: 공의 개수, 1: 가람막의 개수
for _ in range(Q):
    op = input().split()
    if len(op) >= 2:
        op, val = op
        if op == 'push':
            if val == 'w':
                q.append(1)
                cnt[1] += 1
            else:
                if direction == 3:
                    continue
                elif direction == 1:
                    if cnt[1] > 0:
                        q.append(0)
                        cnt[0] += 1
                else:
                    q.append(0)
                    cnt[0] += 1
        elif op == 'count':
            if val == 'b':
                print(cnt[0])
            else:
                print(cnt[1])
        elif op == 'rotate':
            if val == 'l':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            if direction == 1:
                for _ in range(len(q)):
                    if q[0] == 1:
                        break
                    q.popleft()
                    cnt[0] -= 1
            elif direction == 3:
                for _ in range(len(q)):
                    if q[-1] == 1:
                        break
                    q.pop()
                    cnt[0] -= 1
    else:
        if q:
            if q.popleft() == 0:
                cnt[0] -= 1
            else:
                cnt[1] -= 1
                if direction == 1:
                    for _ in range(len(q)):
                        if q[0] == 1:
                            break
                        q.popleft()
                        cnt[0] -= 1
