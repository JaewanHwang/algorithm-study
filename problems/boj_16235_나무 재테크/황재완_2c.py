import sys
from collections import defaultdict

sys.stdin = open("input.txt")
input = sys.stdin.readline

dx, dy = (-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
five_counter = [[0] * N for _ in range(N)]
nutrition = [[5] * N for _ in range(N)]


def simulate():
    new_tree = defaultdict(int)
    for x in range(N):
        for y in range(N):
            five_counter[x][y] = 0
            for ti in range(len(tree[x][y]) - 1, -1, -1):
                if tree[x][y][ti] > nutrition[x][y]:
                    for dti in range(ti + 1):
                        nutrition[x][y] += tree[x][y][dti] // 2
                    tree[x][y] = tree[x][y][ti + 1:]
                    break
                nutrition[x][y] -= tree[x][y][ti]
                tree[x][y][ti] += 1
                if tree[x][y][ti] % 5 == 0:
                    five_counter[x][y] += 1
            nutrition[x][y] += A[x][y]
            if five_counter[x][y] > 0:
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        new_tree[(nx, ny)] += five_counter[x][y]
    for nt in new_tree:
        tree[nt[0]][nt[1]].extend([1] * new_tree[nt])


for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

for _ in range(K):
    simulate()

ans = sum(sum(len(x) for x in row) for row in tree)
print(ans)
