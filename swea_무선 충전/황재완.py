import sys

sys.stdin = open("input.txt", "r")

from itertools import product

dx, dy = (0, 0, 1, 0, -1), (0, -1, 0, 1, 0)


def simulate():
    ax, ay, bx, by = 1, 1, 10, 10
    tot_charge = 0

    for t in range(M + 1):
        candidates = {'A': [0], 'B': [0]}
        for BCi, (X, Y, C, P) in enumerate(BCs, start=1):
            if abs(ax - X) + abs(ay - Y) <= C:
                candidates['A'].append(BCi)
            if abs(bx - X) + abs(by - Y) <= C:
                candidates['B'].append(BCi)

        max_charge = 0
        for case in product(candidates['A'], candidates['B']):
            charge = 0
            if case[0] != 0 and case[1] != 0 and case[0] == case[1]:
                charge = BCs[case[0] - 1][-1]
            else:
                if case[0] != 0:
                    charge += BCs[case[0] - 1][-1]
                if case[1] != 0:
                    charge += BCs[case[1] - 1][-1]
            max_charge = max(max_charge, charge)

        tot_charge += max_charge
        if t == M:
            break
        ax, ay = ax + dx[path_a[t]], ay + dy[path_a[t]]
        bx, by = bx + dx[path_b[t]], by + dy[path_b[t]]

    return tot_charge


T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    path_a = list(map(int, input().split()))
    path_b = list(map(int, input().split()))
    BCs = [list(map(int, input().split())) for _ in range(A)]
    ans = simulate()
    print(f'#{test_case} {ans}')
