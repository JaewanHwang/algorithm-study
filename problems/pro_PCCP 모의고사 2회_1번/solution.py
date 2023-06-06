def solution(command):
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    dirt = 0
    x, y = 0, 0
    for op in command:
        if op == 'R':
            dirt = (dirt + 1) % 4
        elif op == 'L':
            dirt = (dirt - 1) % 4
        elif op == 'G':
            x, y = x + dx[dirt], y + dy[dirt]
        else:
            x, y = x - dx[dirt], y - dy[dirt]
    return [x, y]
