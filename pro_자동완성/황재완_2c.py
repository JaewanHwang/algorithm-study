import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self):
        self.promising = 0
        self.children = dict()


def go(node, i, word):
    node.promising += 1
    if i == len(word):
        return
    if word[i] in node.children:
        go(node.children[word[i]], i + 1, word)
    else:
        node.children[word[i]] = Node()
        go(node.children[word[i]], i + 1, word)


def find(node, i, word):
    if i == len(word):
        return i
    if node.promising == 1:
        return i
    return find(node.children[word[i]], i + 1, word)


def solution(words):
    trie = Node()
    for word in words:
        go(trie, 0, word)
    ans = 0
    for word in words:
        ans += find(trie, 0, word)
    return ans
