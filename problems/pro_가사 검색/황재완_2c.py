import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self):
        self.promising = defaultdict(int)
        self.children = defaultdict(Node)


def solution(words, queries):
    prefix_trie = Node()
    suffix_trie = Node()
    for word in words:
        cur = prefix_trie
        cur.promising[len(word)] += 1
        for c in word:
            cur = cur.children[c]
            cur.promising[len(word)] += 1
        cur = suffix_trie
        cur.promising[len(word)] += 1
        for c in word[::-1]:
            cur = cur.children[c]
            cur.promising[len(word)] += 1

    found = dict()
    ans = [0] * len(queries)
    for qi, query in enumerate(queries):
        if query in found:
            ans[qi] = found[query]
            continue
        if query[-1] == '?':
            cur = prefix_trie
        else:
            cur = suffix_trie

        for c in query if cur == prefix_trie else query[::-1]:
            if c == '?':
                break
            cur = cur.children[c]
        ans[qi] = cur.promising[len(query)]
        found[query] = ans[qi]
    return ans
