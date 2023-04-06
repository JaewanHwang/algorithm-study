import sys
from itertools import product

sys.stdin = open("input.txt", "r")
dx, dy = (0, 0, 1, 0, -1), (0, -1, 0, 1, 0)
T = int(input())


def simulate():
    ans = 0
    ax, ay = 0, 0
    bx, by = 9, 9
    for t in range(M + 1):
        A_candidates = [-1]
        B_candidates = [-1]
        for BCi, (BCx, BCy, C, P) in enumerate(BC):
            if abs(ax - BCx) + abs(ay - BCy) <= C:
                A_candidates.append(BCi)
            if abs(bx - BCx) + abs(by - BCy) <= C:
                B_candidates.append(BCi)
        best_case = 0
        for (A_assigned, B_assigned) in product(A_candidates, B_candidates):
            if A_assigned == B_assigned != -1:
                res = BC[A_assigned][3]
            else:
                A_charge = BC[A_assigned][3] if A_assigned != -1 else 0
                B_charge = BC[B_assigned][3] if B_assigned != -1 else 0
                res = A_charge + B_charge
            best_case = max(best_case, res)
        ans += best_case
        if t == M:
            break
        ad, bd = A_path[t], B_path[t]
        nax, nay = ax + dx[ad], ay + dy[ad]
        nbx, nby = bx + dx[bd], by + dy[bd]
        ax, ay, bx, by = nax, nay, nbx, nby
    return ans


for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    A_path = list(map(int, input().split()))
    B_path = list(map(int, input().split()))
    BC = []
    for _ in range(A):
        x, y, C, P = map(int, input().split())
        BC.append((x - 1, y - 1, C, P))
    ans = simulate()
    print(f'#{test_case} {ans}')
