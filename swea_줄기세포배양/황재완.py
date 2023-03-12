import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def simulate():
    m = {}
    all_cells = set()
    for x in range(N):
        for y in range(M):
            if board[x][y] == 0:
                continue
            m[(x, y)] = [0, board[x][y], board[x][y], 0]
            all_cells.add((x, y))
    for t in range(1, K + 1):
        for x, y in list(m.keys()):
            state, life, ttl, created_at = m[(x, y)]
            if state == 0:  # 비활성 상태
                ttl -= 1
                if ttl == 0:
                    state = 1
                    ttl = life
                m[(x, y)] = [state, life, ttl, created_at]
            elif state == 1:  # 활성 상태
                if ttl == life:  # 첫 활성상태
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if (nx, ny) not in all_cells or (
                                (nx, ny) in m and m[(nx, ny)][0] == 0 and m[(nx, ny)][3] == t and m[(nx, ny)][
                            1] < life):
                            m[(nx, ny)] = [0, life, life, t]
                            all_cells.add((nx, ny))
                ttl -= 1
                if ttl == 0:
                    m.pop((x, y))
                else:
                    m[(x, y)] = [state, life, ttl, created_at]
    return len(list(filter(lambda key: m[key] and m[key][0] != 2, m.keys())))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {simulate()}')
