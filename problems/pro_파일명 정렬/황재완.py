# 풀이1
def solution(files):
    answer = []
    for OREDER, file in enumerate(files):
        in_number = False
        number_end = len(file)
        for i in range(len(file)):
            if not in_number and file[i].isdigit():
                in_number = True
                number_start = i
            elif in_number and not file[i].isdigit():
                number_end = i
                break

        HEAD = file[:number_start].upper()
        NUMBER = int(file[number_start:number_end])
        answer.append((HEAD, NUMBER, OREDER, file))

    answer.sort()
    answer = list(map(lambda x: x[3], answer))
    return answer


# 풀이2
import re


def solution(files):
    answer = []
    p = re.compile('(\D+)(\d+)')
    for OREDER, file in enumerate(files):
        m = p.match(file)
        HEAD = m.group(1).upper()
        NUMBER = int(m.group(2))
        answer.append((HEAD, NUMBER, OREDER))

    answer.sort()
    answer = list(map(lambda x: files[x[2]], answer))
    return answer
