import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
Ais = list(map(int, input().split()))
ops = list(map(int, input().split()))
ans_max = -1_000_000_000
ans_min = 1_000_000_000


def go(n, tot):
    global ans_max, ans_min
    if n == N - 1:
        ans_max = max(ans_max, tot)
        ans_min = min(ans_min, tot)
        return
    if ops[0] > 0:
        ops[0] -= 1
        go(n + 1, tot + Ais[n + 1])
        ops[0] += 1
    if ops[1] > 0:
        ops[1] -= 1
        go(n + 1, tot - Ais[n + 1])
        ops[1] += 1
    if ops[2] > 0:
        ops[2] -= 1
        go(n + 1, tot * Ais[n + 1])
        ops[2] += 1
    if ops[3] > 0:
        ops[3] -= 1
        go(n + 1, tot // Ais[n + 1] if tot >= 0 else - (- tot // Ais[n + 1]))
        ops[3] += 1


go(0, Ais[0])

print(ans_max, ans_min, sep='\n')
