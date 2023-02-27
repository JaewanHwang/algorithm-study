# 풀이1
import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self):
        self.promising = 0
        self.word = None
        self.children = dict()


def go(cur):
    if cur.word:
        cur.promising += 1

    for child in cur.children:
        cur.promising += go(cur.children[child])

    return cur.promising


def solution(words):
    trie = Node()  # [단어 존재 여부, children{}]
    for word in words:
        cur = trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()

            cur = cur.children[char]
        cur.word = word

    go(trie)

    ans = 0
    for word in words:
        cur = trie
        for cnt, char in enumerate(word, start=1):
            cur = cur.children[char]
            if cur.promising == 1:
                break
        ans += cnt

    return ans


# 풀이2
class Node:
    def __init__(self):
        self.promising = 0
        self.word = None
        self.children = dict()


def solution(words):
    trie = Node()  # [단어 존재 여부, children{}]
    for word in words:
        cur = trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
            cur.promising += 1
        cur.word = word

    ans = 0
    for word in words:
        cur = trie
        for cnt, char in enumerate(word, start=1):
            cur = cur.children[char]
            if cur.promising == 1:
                break
        ans += cnt

    return ans
