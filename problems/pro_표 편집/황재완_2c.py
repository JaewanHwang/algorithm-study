def solution(n, k, cmd):
    table = [[i - 1, i + 1] for i in range(n)]
    removed = [False] * n
    history = []
    for operation in cmd:
        if len(operation) == 1:
            if operation == 'C':
                removed[k] = True
                history.append(k)
                prev, next = table[k]
                if prev >= 0:
                    table[prev][1] = next
                if next < n:
                    table[next][0] = prev

                if next == n:
                    k = prev
                else:
                    k = next

            else:
                recovered = history.pop()
                removed[recovered] = False
                prev, next = table[recovered]
                if prev >= 0:
                    table[prev][1] = recovered
                if next < n:
                    table[next][0] = recovered

        else:
            op, X = operation.split()
            d = 0 if op == 'U' else 1
            for _ in range(int(X)):
                k = table[k][d]

    ans = ''.join(map(lambda x: 'O' if not removed[x] else 'X', range(n)))
    return ans
