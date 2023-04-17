import re


def solution(m, musicinfos):
    p = re.compile(m if m[-1] == '#' else f'{m + "[^#]"}|{m}$')
    candidates = []

    for o in range(len(musicinfos)):
        st, et, title, sounds = musicinfos[o].split(',')
        hh, mm = map(int, st.split(':'))
        st = hh * 60 + mm
        hh, mm = map(int, et.split(':'))
        et = hh * 60 + mm
        rt = et - st

        cur = 0
        music = []
        while cur < len(sounds):
            if cur + 1 < len(sounds) and sounds[cur + 1] == '#':
                music.append(sounds[cur: cur + 2])
                cur += 2
            else:
                music.append(sounds[cur])
                cur += 1

        if len(music) < rt:
            pattern = music * (rt // len(music)) + music[:len(music) % rt]
        else:
            pattern = music[:rt]

        if p.search(''.join(pattern)):
            candidates.append((-rt, o, title))

    if not candidates:
        return '(None)'
    else:
        _, _, answer = min(candidates)
        return answer
