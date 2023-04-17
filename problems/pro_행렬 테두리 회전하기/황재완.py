def solution(rows, columns, queries):
    m = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    ans = []
    for query in queries:

        x1, y1, x2, y2 = map(lambda x: int(x) - 1, query)
        tmp = m[x1][y1]
        res = tmp
        for x in range(x1, x2):
            m[x][y1] = m[x + 1][y1]
            res = min(res, m[x][y1])
        for y in range(y1, y2):
            m[x2][y] = m[x2][y + 1]
            res = min(res, m[x2][y])
        for x in range(x2, x1, -1):
            m[x][y2] = m[x - 1][y2]
            res = min(res, m[x][y2])
        for y in range(y2, y1 + 1, -1):
            m[x1][y] = m[x1][y - 1]
            res = min(res, m[x1][y])
        m[x1][y1 + 1] = tmp
        ans.append(res)
    return ans
