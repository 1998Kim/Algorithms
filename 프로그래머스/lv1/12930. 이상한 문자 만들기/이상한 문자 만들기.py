def solution(s):
    s_lst = s.split(" ")
    answer = ''
    
    for i, v in enumerate(s_lst):
        for j in range(len(v)):
            if j % 2 == 0:
                answer += v[j].upper()
            else:
                answer += v[j].lower()
        if i != (len(s_lst) - 1):
            answer += ' '
    return answer