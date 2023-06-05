def solution(s):
    s_int = sorted(list(map(int, s.split())))
    answer = str(s_int[0]) + ' ' + str(s_int[-1])
    return answer