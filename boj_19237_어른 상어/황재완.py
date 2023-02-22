import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

N, M, k = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
shark_map = dict()
for x in range(N):
    for y in range(N):
        if m[x][y] >= 1:
            shark_map[m[x][y]] = [x, y]
            m[x][y] = [m[x][y], k]  # 상어 번호, 남은 시간
        else:
            m[x][y] = []
for i, d in enumerate(map(lambda x: int(x) - 1, input().split()), start=1):
    shark_map[i].append(d)
for i in range(1, M + 1):
    priority = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(4)]
    shark_map[i].append(priority)

t = 0
while len(shark_map) > 1 and t <= 1001:
    # 1. 상어 이동
    s = [[0] * N for _ in range(N)]
    smell_list = []
    for num in sorted(shark_map):
        x, y, d, priority = shark_map[num]
        for nd in priority[d]:
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < N and 0 <= ny < N and not m[nx][ny]:
                break
        else:
            for nd in priority[d]:
                nx, ny = x + dx[nd], y + dy[nd]
                if 0 <= nx < N and 0 <= ny < N and m[nx][ny] and m[nx][ny][0] == num:
                    break
        if s[nx][ny]:  # 이미 있다면
            shark_map.pop(num)
            continue
        s[nx][ny] = num
        smell_list.append((nx, ny, [num, k]))
        shark_map[num] = [nx, ny, nd, priority]
    # 2. 냄새 1씩 차감
    for x in range(N):
        for y in range(N):
            if m[x][y]:
                m[x][y][1] -= 1
                if m[x][y][1] == 0:
                    m[x][y] = []
    for x, y, smell in smell_list:
        m[x][y] = smell
    t += 1

ans = t if t <= 1000 else -1
print(ans)
