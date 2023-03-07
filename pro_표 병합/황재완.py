p = [-1] * 2500
table = [''] * 2500
merged_cells = [[i] for i in range(2500)]


def find_root(i):
    if p[i] == -1:
        return i
    p[i] = find_root(p[i])
    return p[i]


def merge(r1, c1, r2, c2):
    root1, root2 = find_root(r1 * 50 + c1), find_root(r2 * 50 + c2)
    if root1 == root2:
        return

    if table[root1] and table[root2]:
        p[root2] = root1
        merged_cells[root1].extend(merged_cells[root2])
        merged_cells[root2] = [root2]
        table[root2] = ''

    elif not table[root1] and table[root2]:
        p[root1] = root2
        merged_cells[root2].extend(merged_cells[root1])
        merged_cells[root1] = [root1]
    else:
        p[root2] = root1
        merged_cells[root1].extend(merged_cells[root2])
        merged_cells[root2] = [root2]


def unmerge(r, c):
    root = find_root(50 * r + c)
    table[50 * r + c] = table[root]
    if 50 * r + c != root:
        table[root] = ''
    for cell in merged_cells[root]:
        p[cell] = -1
    merged_cells[root] = [root]


def solution(commands):
    global p, talbe
    ans = []
    for command in commands:
        op = command.split()
        if op[0] == 'UPDATE':
            if len(op) == 4:
                r, c, value = op[1:]
                r, c = int(r) - 1, int(c) - 1
                table[find_root(50 * r + c)] = value
            else:
                value1, value2 = op[1:]
                for i in range(2500):
                    root = find_root(i)
                    if table[root] == value1:
                        table[root] = value2
        elif op[0] == 'MERGE':
            merge(*map(lambda x: int(x) - 1, op[1:]))

        elif op[0] == 'UNMERGE':
            unmerge(*map(lambda x: int(x) - 1, op[1:]))

        elif op[0] == 'PRINT':
            r, c = map(lambda x: int(x) - 1, op[1:])
            root = find_root(50 * r + c)
            ans.append(table[root] if table[root] else 'EMPTY')

    return ans
