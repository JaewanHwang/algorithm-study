import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, L = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def go(m):
    global ans
    for row in m:
        c = [False] * N
        cant = False
        for i in range(N - 1):
            if row[i] == row[i + 1]:
                continue
            elif abs(row[i] - row[i + 1]) > 1:
                cant = True
                break
            elif row[i] > row[i + 1]:
                for j in range(L):
                    if i + 1 + j == N or row[i + 1 + j] != row[i + 1] or c[i + 1 + j]:
                        cant = True
                        break
                    c[i + 1 + j] = True
            else:
                for j in range(L):
                    if i - j < 0 or row[i - j] != row[i] or c[i - j]:
                        cant = True
                        break
                    c[i - j] = True
            if cant:
                break
        if not cant:
            ans += 1


go(m)
go(list(zip(*m)))

print(ans)
