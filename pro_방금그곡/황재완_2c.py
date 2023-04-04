def transform(sound):
    mapping = {'C#': '1', 'D#': '2', 'F#': '3', 'G#': '4', 'A#': '5'}
    for key in mapping:
        new_sound = sound.replace(key, mapping[key])
        sound = new_sound
    return sound


def solution(m, musicinfos):
    m = transform(m)
    candidates = []
    for order, musicinfo in enumerate(musicinfos):
        s, e, title, sound = musicinfo.split(',')
        sound = transform(sound)
        s = int(s[:2]) * 60 + int(s[3:])
        e = int(e[:2]) * 60 + int(e[3:])
        time = e - s
        period = len(sound)
        track = ''
        for i in range(max(time, len(m))):
            track += sound[i % period]
        if m in track:
            candidates.append((time, order, title))
    if candidates:
        _, _, ans = max(candidates, key=lambda x: (x[0], -x[1]))
        return ans
    else:
        return '(None)'
