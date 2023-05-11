def solution(s):
    answer = True
    s = s.lower()
    num_p, num_y = 0, 0
    
    for i in s:
        if i == 'p':
            num_p += 1
        elif i == 'y':
            num_y += 1

    if num_p != num_y:
        answer = False


    return answer