import sys
from collections import Counter

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
files = Counter()
for _ in range(N):
    filename = input().rstrip()
    fn, ext = filename.split('.')
    files[ext] += 1
for ext in sorted(files):
    print(ext, files[ext])
