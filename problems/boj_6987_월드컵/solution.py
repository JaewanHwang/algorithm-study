import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def go(i):
    if i == 15:
        if sum(sum(row) for row in record) == 0:
            return True
        else:
            return False

    x, y = cases[i]
    # 1. x가 이겼을 때
    if record[x][0] > 0 and record[y][2] > 0:
        record[x][0] -= 1
        record[y][2] -= 1
        if go(i + 1):
            return True
        record[x][0] += 1
        record[y][2] += 1
    # 2. y가 이겼을 때
    if record[x][2] > 0 and record[y][0] > 0:
        record[x][2] -= 1
        record[y][0] -= 1
        if go(i + 1):
            return True
        record[x][2] += 1
        record[y][0] += 1
    # 3. 무승부
    if record[x][1] > 0 and record[y][1] > 0:
        record[x][1] -= 1
        record[y][1] -= 1
        if go(i + 1):
            return True
        record[x][1] += 1
        record[y][1] += 1
    return False


ans = []
cases = []
for i in range(6):
    for j in range(i + 1, 6):
        cases.append((i, j))

for _ in range(4):
    line = list(map(int, input().split()))
    record = [line[i: i + 3] for i in range(0, 18, 3)]
    ans.append(int(go(0)))
print(*ans)
