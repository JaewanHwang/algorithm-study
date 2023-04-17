# 풀이 1
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0, -1, 1, 1, -1), (0, 0, -1, 1, 1, 1, -1, -1)
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
m = [[[] for _ in range(N)] for _ in range(N)]
n = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    m[x - 1][y - 1].append(z)
for x in range(N):
    for y in range(N):
        m[x][y].sort()
for _ in range(K):
    # 봄
    for x in range(N):
        for y in range(N):
            for i, age in enumerate(m[x][y]):
                if n[x][y] >= age:
                    n[x][y] -= age
                    m[x][y][i] += 1
                else:
                    # 여름
                    n[x][y] += sum(map(lambda x: x // 2, m[x][y][i:]))
                    m[x][y] = m[x][y][:i]
                    break
    # 가을
    for x in range(N):
        for y in range(N):
            for i, age in enumerate(m[x][y]):
                if age % 5 == 0:
                    for d in range(8):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            m[nx][ny].append(1)
    for x in range(N):
        for y in range(N):
            m[x][y].sort()
            # 겨울
            n[x][y] += A[x][y]

ans = sum(sum(map(len, row)) for row in m)
print(ans)

# 풀이2
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0, -1, 1, 1, -1), (0, 0, -1, 1, 1, 1, -1, -1)
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
m = [[[] for _ in range(N)] for _ in range(N)]
n = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    m[x - 1][y - 1].append(z)
for x in range(N):
    for y in range(N):
        m[x][y] = deque(sorted(m[x][y]))
for _ in range(K):
    # 봄
    for x in range(N):
        for y in range(N):
            for i, age in enumerate(m[x][y]):
                if n[x][y] >= age:
                    n[x][y] -= age
                    m[x][y][i] += 1
                else:
                    # 여름
                    for j in range(i, len(m[x][y])):
                        n[x][y] += m[x][y].pop() // 2
                    break
            # 겨울
            n[x][y] += A[x][y]
    # 가을
    for x in range(N):
        for y in range(N):
            for i, age in enumerate(m[x][y]):
                if age % 5 == 0:
                    for d in range(8):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            m[nx][ny].appendleft(1)

ans = sum(sum(map(len, row)) for row in m)
print(ans)