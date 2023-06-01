def solution(queries):
    def go(n, cur):
        if n == N - 1:
            return cur
        if cur == 'Rr':
            children = ['RR', 'Rr', 'Rr', 'rr']
        elif cur == 'RR':
            children = ['RR'] * 4
        else:
            children = ['rr'] * 4
        return go(n + 1, children[path[n]])

    ans = []
    for N, P in queries:
        path = []
        P -= 1
        for _ in range(N - 1):
            path.append(P % 4)
            P //= 4
        path = path[::-1]
        ans.append(go(0, 'Rr'))
    return ans
