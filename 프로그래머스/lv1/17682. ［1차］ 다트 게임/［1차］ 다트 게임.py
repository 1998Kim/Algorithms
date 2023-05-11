def solution(dartResult):
    answer = 0
    
    result = dartResult.replace('10', 't')
    score = []
    
    for i in result:
        if i.isdigit():
            score.append(int(i))
        elif i == 't':
            score.append(10)
        
        if i == 'S':
            score[-1] = score[-1] ** 1
        elif i == 'D':
            score[-1] = score[-1] ** 2
        elif i == 'T':
            score[-1] = score[-1] ** 3
            
        if i == '*':
            if len(score) >= 2:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * (-1)
            
    answer = sum(score)
    
    return answer