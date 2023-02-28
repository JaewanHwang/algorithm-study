from collections import defaultdict


class Node:
    def __init__(self):
        self.children = dict()
        self.len_counter = defaultdict(int)


def make_trie(trie1, trie2, words):
    for word in words:
        cur1, cur2 = trie1, trie2
        for i in range(len(word)):
            j = len(word) - i
            cur1.len_counter[j] += 1
            cur2.len_counter[j] += 1
            char1, char2 = word[i], word[j - 1]
            if char1 not in cur1.children:
                cur1.children[char1] = Node()
            if char2 not in cur2.children:
                cur2.children[char2] = Node()
            cur1 = cur1.children[char1]
            cur2 = cur2.children[char2]


def solution(words, queries):
    # trie1: 정방향 트라이, trie2: 역방향 트라이
    trie1, trie2 = Node(), Node()
    make_trie(trie1, trie2, words)
    ans = [0] * len(queries)
    for i, query in enumerate(queries):
        if query[0] == '?' and query[-1] == '?':
            ans[i] = trie1.len_counter[len(query)]
        else:
            cur, j = trie1 if query[-1] == '?' else trie2, 0
            if query[0] == '?':
                query = query[::-1]
            while query[j] in cur.children and query[j] != '?':
                cur = cur.children[query[j]]
                j += 1
            ans[i] = cur.len_counter[len(query) - j] if query[j] == '?' else 0
    return ans


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["???to", "????o", "fr???", "fro???", "pro?"]))
