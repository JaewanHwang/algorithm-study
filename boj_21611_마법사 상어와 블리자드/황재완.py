import sys
from collections import deque

sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
dir_map = {0: 2, 1: 0, 2: 3, 3: 1}

N, M = map(int, input().split())
SIZE = N * N - 1
cx, cy = N // 2, N // 2
m = [list(map(int, input().split())) for _ in range(N)]
m[cx][cy] = -1
ans = [0] * 4


def go(x, y, d, q):
    if m[x][y] > 0:
        q.append(m[x][y])
    m[x][y] = -1
    if x == 0 and y == 0:
        return

    nd = (d + 1) % 4
    nx, ny = x + dx[nd], y + dy[nd]
    if not (0 <= nx < N and 0 <= ny < N and m[nx][ny] != -1):
        nx, ny = x + dx[d], y + dy[d]
        nd = d
    go(nx, ny, nd, q)


def insert(x, y, d, q):
    if not q:
        return
    m[x][y] = q.popleft()

    nd = (d + 1) % 4
    nx, ny = x + dx[nd], y + dy[nd]
    if not (0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0):
        nx, ny = x + dx[d], y + dy[d]
        nd = d
    insert(nx, ny, nd, q)


def simulate(di, si):
    global m
    # 1. 얼음 파편 던지기
    for i in range(1, si + 1):
        nx, ny = cx + i * dx[di], cy + i * dy[di]
        m[nx][ny] = 0
    q = deque()
    go(cx, cy - 1, 0, q)

    # 2. 구슬 폭발
    while True:
        cnt = 0
        stack = deque()
        ol = len(q)
        while q:
            num = q.popleft()
            if not stack or stack[-1] != num or not q:
                if cnt >= 4:
                    for _ in range(cnt):
                        ans[stack.pop()] += 1
                stack.append(num)
                cnt = 1
            elif stack[-1] == num:
                stack.append(num)
                cnt += 1
        if ol == len(stack):
            # 3. 구슬 변형
            q = deque()
            cnt, last = 1, 0
            for i in range(1, len(stack) + 1):
                if i == len(stack) or stack[i] != stack[last]:
                    q.append(cnt)
                    q.append(stack[last])
                    last = i
                    cnt = 1
                else:
                    cnt += 1
                if len(q) == SIZE:
                    break
            break
        q = stack

    # 4. 구슬 집어 넣기
    m = [[0] * N for _ in range(N)]
    m[cx][cy] = -1
    insert(cx, cy - 1, 0, q)


for _ in range(M):
    di, si = map(int, input().split())
    simulate(dir_map[di - 1], si)

ans = ans[1] * 1 + ans[2] * 2 + ans[3] * 3
print(ans)
