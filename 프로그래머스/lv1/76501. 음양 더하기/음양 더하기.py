def solution(absolutes, signs):
    answer = 0
    
    for i, v in enumerate(signs):
        if v:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * (-1)
    return answer