import string


def solution(x):
    straight = dict(zip(string.ascii_lowercase, range(1,27)))
    revers = dict(zip(reversed(string.ascii_lowercase), range(1,27)))
    answer = ""
    for n in x:
        if n.islower():
            position = (revers.get(n))
            for key, value in straight.items():
                if value == position:
                    answer += key
        else:
            answer += n
    return answer


print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
