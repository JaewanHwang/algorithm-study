import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    s = list(map(lambda x: int(x) if x.isdigit() and int(x) < 10 else ord(x) - ord('A') + 10, input()))
    all_case = set()
    for i in range(N // 4):
        for _ in range(4):
            res = 0
            for j in range(N // 4):
                res = 16 * res + s[i]
                i = (i + 1) % len(s)
            all_case.add(res)
    print(f'#{test_case} {sorted(all_case, reverse=True)[K - 1]}')
