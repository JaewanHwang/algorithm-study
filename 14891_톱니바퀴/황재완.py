import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

g = [input().rstrip() for _ in range(4)]
K = int(input())

for _ in range(K):
    n, d = map(int, input().split())
    n -= 1
    rotates = [(n, d)]
    cd = d
    for l in range(n - 1, -1, -1):
        if g[l + 1][6] != g[l][2]:
            cd = -cd
            rotates.append((l, cd))
        else:
            break
    cd = d
    for r in range(n + 1, 4):
        if g[r - 1][2] != g[r][6]:
            cd = -cd
            rotates.append((r, cd))
        else:
            break
    for n, d in rotates:
        if d == 1:
            g[n] = g[n][7] + g[n][:7]
        else:
            g[n] = g[n][1:] + g[n][0]



ans = 0
for n in range(4):
    ans += 2 ** n if g[n][0] == '1' else 0
print(ans)