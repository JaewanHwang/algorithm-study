import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    cur_max = stock.pop()
    ans = 0
    for i in range(len(stock) - 1, -1, -1):
        price = stock[i]
        if price < cur_max:
            ans += cur_max - price
        else:
            cur_max = price
    print(ans)
