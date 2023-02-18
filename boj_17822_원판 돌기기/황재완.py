import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, T = map(int, input().split())
m = [[0] * M] + [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    xi, di, ki = map(int, input().split())
    di = 1 if di == 0 else -1
    for x in range(xi, N + 1, xi):
        tmp = [0] * M
        for i in range(M):
            tmp[(i + di * ki) % M] = m[x][i]
        m[x] = tmp
    total = 0
    cnt = 0
    remove_set = set()
    for i in range(1, N + 1):
        for j in range(M):
            if m[i][j] == 0:
                continue
            cnt += 1
            total += m[i][j]
            if i - 1 >= 1 and m[i - 1][j] == m[i][j]:
                remove_set.add((i, j))
                remove_set.add((i - 1, j))
            if i + 1 <= N and m[i + 1][j] == m[i][j]:
                remove_set.add((i, j))
                remove_set.add((i + 1, j))
            if m[i][j] == m[i][(j - 1) % M]:
                remove_set.add((i, j))
                remove_set.add((i, (j - 1) % M))
            if m[i][j] == m[i][(j + 1) % M]:
                remove_set.add((i, j))
                remove_set.add((i, (j + 1) % M))

    if not remove_set and cnt > 0:
        avg = total / cnt
        for i in range(1, N + 1):
            for j in range(M):
                if m[i][j] == 0:
                    continue
                if m[i][j] > avg:
                    m[i][j] -= 1
                elif m[i][j] < avg:
                    m[i][j] += 1
    for i, j in remove_set:
        m[i][j] = 0

ans = sum(map(sum, m))
print(ans)
