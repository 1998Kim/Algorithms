from itertools import combinations_with_replacement as cwp

def solution(n, info):
    answer = []
    cases = list(cwp(range(11), r=n))

    for case in cases:
        info_ryan = [0] * 11
        score_ryan, score_apeach = 0, 0
        
        for point in case:
            info_ryan[10-point] += 1

        for index in range(11):
            if info[index] == 0 and info_ryan[index] == 0:
                continue
            
            if info[index] >= info_ryan[index]:
                score_apeach += (10 - index)
            else:
                score_ryan += (10 - index)
                
        diff = score_ryan - score_apeach
        
        if diff > 0:
            answer.append((diff, info_ryan))
        
    answer.sort(key=lambda x: (x[0], x[1][::-1]), reverse=True)
    
    if len(answer) == 0:
        return [-1]
        
    return answer[0][1]