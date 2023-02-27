import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self):
        self.promising = 0
        self.word = None
        self.childs = dict()


def go(cur):
    if cur.word != None:
        cur.promising += 1

    for child in cur.childs:
        cur.promising += go(cur.childs[child])

    return cur.promising


def solution(words):
    trie = Node()  # [단어 존재 여부, child{}]
    for word in words:
        cur = trie
        for i in range(len(word)):
            char = word[i]
            if char not in cur.childs:
                child = Node()
                cur.childs[char] = child
            cur = cur.childs[char]
            if i == len(word) - 1:
                cur.word = word
    go(trie)
    ans = 0
    for word in words:
        cur = trie
        for i in range(len(word)):
            char = word[i]
            cur = cur.childs[char]
            if cur.promising == 1:
                ans += i + 1
                break
        else:
            ans += i + 1

    return ans
