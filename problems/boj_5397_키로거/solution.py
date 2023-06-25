import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lstk, rstk = [], []
    pwd = input().rstrip()
    for char in pwd:
        if char == '<':
            if lstk:
                rstk.append(lstk.pop())
        elif char == '>':
            if rstk:
                lstk.append(rstk.pop())
        elif char == '-':
            if lstk:
                lstk.pop()
        else:
            lstk.append(char)
    print(''.join(lstk + rstk[::-1]))
