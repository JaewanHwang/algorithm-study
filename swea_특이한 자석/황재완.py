import sys

sys.stdin = open("input.txt", "r")


def rotate(gears, gi, d):
    if d == 1:
        gears[gi] = gears[gi][-1:] + gears[gi][:-1]
    else:
        gears[gi] = gears[gi][1:] + gears[gi][:1]


def simulate():
    for gi, d in operations:
        operation_list = [(gi, d)]
        cd = d
        for ri in range(gi + 1, 5):
            if gears[ri][6] != gears[ri - 1][2]:
                cd = -cd
                operation_list.append((ri, cd))
            else:
                break
        cd = d
        for li in range(gi - 1, 0, -1):
            if gears[li][2] != gears[li + 1][6]:
                cd = -cd
                operation_list.append((li, cd))
            else:
                break
        for i, d in operation_list:
            rotate(gears, i, d)
    res = 0
    for gi in range(1, 5):
        res += gears[gi][0] * (2 ** (gi - 1))
    return res


T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    gears = [0] + [list(map(int, input().split())) for _ in range(4)]
    operations = [list(map(int, input().split())) for _ in range(K)]
    ans = simulate()
    print(f'#{test_case} {ans}')
