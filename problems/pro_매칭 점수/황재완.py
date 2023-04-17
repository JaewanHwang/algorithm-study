import re
from collections import defaultdict


def solution(word, pages):
    websites = dict()
    backlinks = defaultdict(list)
    scores = [0] * len(pages)
    word = word.upper()
    for i, html in enumerate(pages):
        cnt = len(list(filter(lambda x: x.upper() == word, re.split(r'[^a-zA-Z]', html))))
        url = re.search(r'<meta property=\"og:url\" content=\"https://(\S+)\"', html).group(1)
        links = re.findall(r'<a href=\"https://(\S+)\"', html)
        websites[url] = [i, cnt, len(links)]
        for link in links:
            backlinks[link].append(url)
    for url in websites:
        i, cnt, _ = websites[url]
        scores[i] = cnt
        for backlink in backlinks[url]:
            scores[i] += websites[backlink][1] / websites[backlink][2]
    ans = scores.index(max(scores))
    print(websites)
    return ans
