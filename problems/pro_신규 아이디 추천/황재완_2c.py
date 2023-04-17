def solution(new_id):
    first = new_id.lower()
    second = ''
    for c in first:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):
            second += c
    while True:
        third = second.replace('..', '.')
        if len(third) == len(second):
            break
        second = third
    fourth = third.strip('.')
    if not fourth:
        fifth = 'a'
    else:
        fifth = fourth
    if len(fifth) >= 16:
        sixth = fifth[:15]
        sixth = sixth.rstrip('.')
    else:
        sixth = fifth
    if len(sixth) <= 2:
        ans = sixth + sixth[-1] * (3 - len(sixth))
    else:
        ans = sixth
    return ans
