import re
from collections import defaultdict


def solution(word, pages):
    url2index = dict()
    index2url = [0] * len(pages)
    scores = [[0, 0] for _ in range(len(pages))]
    ans = [0] * len(pages)
    links = defaultdict(list)
    for pi, page in enumerate(pages):
        scores[pi][0] = re.split(r'[^A-Z]', page.upper()).count(word.upper())
        url = re.search(r'<meta property="og:url" content="(\S+)"', page).group(1)
        index2url[pi] = url
        url2index[url] = pi
        for to in re.findall(r'<a href="(\S+)"', page):
            links[to].append(url)
            scores[pi][1] += 1

    for pi in range(len(pages)):
        tot = 0
        for link in links[index2url[pi]]:
            tot += scores[url2index[link]][0] / scores[url2index[link]][1]
        ans[pi] = scores[pi][0] + tot

    ans = max(range(len(pages)), key=lambda x: (ans[x], -x))
    return ans
