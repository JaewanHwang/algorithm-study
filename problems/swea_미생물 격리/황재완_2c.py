import sys

sys.stdin = open("input.txt", "r")

T = int(input())
change_dir = [0, 0, 2, 3, 1]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    cells = dict()
    for _ in range(K):
        x, y, s, d = map(int, input().split())
        cells[(x, y)] = (s, change_dir[d], -1)
    for _ in range(M):
        new_cells = dict()
        for (x, y) in cells:
            s, d, _ = cells[(x, y)]
            nx, ny = x + dx[d], y + dy[d]
            if 1 <= nx < N - 1 and 1 <= ny < N - 1:
                if (nx, ny) in new_cells:
                    cur_s, max_d, max_s = new_cells[(nx, ny)]
                    if max_s < s:
                        new_cells[(nx, ny)] = (cur_s + s, d, s)
                    else:
                        new_cells[(nx, ny)] = (cur_s + s, max_d, max_s)
                else:
                    new_cells[(nx, ny)] = (s, d, s)
            else:
                if s // 2 > 0:
                    new_cells[(nx, ny)] = (s // 2, (d + 2) % 4, -1)
        cells = new_cells
    ans = 0
    for s, _, _ in cells.values():
        ans += s
    print(f'#{test_case} {ans}')
