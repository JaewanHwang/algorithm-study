def solution(input_string):
    alphabets = set(input_string)
    ans = set()
    pos = {c: -1 for c in alphabets}
    for i, c in enumerate(input_string):
        if pos[c] != -1 and i - pos[c] > 1:
            ans.add(c)
        pos[c] = i
    if not ans:
        return 'N'
    return ''.join(sorted(ans))
