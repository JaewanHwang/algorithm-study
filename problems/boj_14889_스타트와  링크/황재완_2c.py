import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
TEAM_SIZE = N // 2
m = [list(map(int, input().split())) for _ in range(N)]


def go(n, ai, bi):
    if ai > TEAM_SIZE or bi > TEAM_SIZE:
        return float('inf')
    if n == N:
        return calculate()
    res = float('inf')
    if ai < TEAM_SIZE:
        tmp = A_team[ai]
        A_team[ai] = n
        res = min(res, go(n + 1, ai + 1, bi))
        A_team[ai] = tmp
    if bi < TEAM_SIZE:
        tmp = B_team[bi]
        B_team[bi] = n
        res = min(res, go(n + 1, ai, bi + 1))
        B_team[bi] = tmp
    return res


def calculate():
    A_power, B_power = 0, 0
    for i in range(TEAM_SIZE):
        for j in range(i + 1, TEAM_SIZE):
            A_power += m[A_team[i]][A_team[j]] + m[A_team[j]][A_team[i]]
            B_power += m[B_team[i]][B_team[j]] + m[B_team[j]][B_team[i]]
    return abs(A_power - B_power)


A_team, B_team = [0] * TEAM_SIZE, [0] * TEAM_SIZE
print(go(0, 0, 0))
