def solution(s):
    len_s = len(s)
    if len_s == 4 or len_s == 6:
        try:
            int(s)
            answer = True
        except:
            answer = False
    else:
        answer = False
    return answer