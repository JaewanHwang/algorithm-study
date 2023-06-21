import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    word = list(input().rstrip())
    i = len(word) - 1
    while i > 0 and word[i - 1] >= word[i]:
        i -= 1
    if i == 0:
        print(''.join(word))
        continue

    j = len(word) - 1
    while word[j] <= word[i - 1]:
        j -= 1
    word[i - 1], word[j] = word[j], word[i - 1],

    k = len(word) - 1
    while i < k:
        word[i], word[k] = word[k], word[i]
        i += 1
        k -= 1
    print(''.join(word))
