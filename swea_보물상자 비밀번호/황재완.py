import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num_l = list(input().rstrip())
    num_s = set()
    for _ in range(N // 4):
        num_l = num_l[-1:] + num_l[:-1]
        for i in range(4):
            num_s.add(int('0x' + ''.join(num_l[i * N // 4: N // 4 * (i + 1)]), 16))
    print(f'#{test_case} {sorted(num_s, reverse=True)[K - 1]}')
