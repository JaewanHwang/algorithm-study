def solution(commands):
    SIZE = 50
    table = [[(i, j) for j in range(SIZE + 1)] for i in range(SIZE + 1)]
    data = [[''] * (SIZE + 1) for _ in range(SIZE + 1)]
    ans = []
    for command in commands:
        op, *operands = command.split()
        if op == 'UPDATE':
            if len(operands) == 3:
                r, c, value = operands
                r, c = table[int(r)][int(c)]
                data[r][c] = value
            else:
                value1, value2 = operands
                for r in range(1, SIZE + 1):
                    for c in range(1, SIZE + 1):
                        if data[r][c] == value1:
                            data[r][c] = value2
        elif op == 'MERGE':
            r1, c1, r2, c2 = map(int, operands)
            r1, c1 = table[r1][c1]
            r2, c2 = table[r2][c2]
            if (r1, c1) == (r2, c2):
                continue
            if not (data[r1][c1] and data[r2][c2]):
                data[r1][c1] += data[r2][c2]
            data[r2][c2] = ''
            for r in range(1, SIZE + 1):
                for c in range(1, SIZE + 1):
                    if table[r][c] == (r2, c2):
                        table[r][c] = table[r1][c1]

        elif op == 'UNMERGE':
            sr, sc = map(int, operands)
            r, c = table[sr][sc]
            tmp = data[r][c]
            for x in range(1, SIZE + 1):
                for y in range(1, SIZE + 1):
                    if table[x][y] == (r, c):
                        table[x][y] = (x, y)
                        data[x][y] = ''
            data[sr][sc] = tmp

        else:
            r, c = map(int, operands)
            r, c = table[r][c]
            ans.append(data[r][c] if data[r][c] else 'EMPTY')

    return ans


print(solution(
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1",
     "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
