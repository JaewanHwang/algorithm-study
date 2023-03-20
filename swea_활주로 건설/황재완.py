import sys

sys.stdin = open("input.txt", "r")


def check(row):
    y = 0
    built = [False] * N
    while y < N - 1:
        if row[y] == row[y + 1]:
            ...
        elif row[y] - row[y + 1] == 1 and y + X < N:
            height = row[y + 1]
            for ty in range(y + 1, y + 1 + X):
                if row[ty] != height or built[ty]:
                    return 0
                built[ty] = True
        elif row[y + 1] - row[y] == 1 and y - X + 1 >= 0:
            height = row[y]
            for ty in range(y, y - X, -1):
                if row[ty] != height or built[ty]:
                    return 0
                built[ty] = True
        else:
            return 0
        y += 1
    return 1


def simulate(m):
    res = 0
    for x in range(N):
        res += check(m[x])
    m = list(zip(*m))
    for x in range(N):
        res += check(m[x])
    return res


T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    ans = simulate(m)
    print(f'#{test_case} {ans}')
