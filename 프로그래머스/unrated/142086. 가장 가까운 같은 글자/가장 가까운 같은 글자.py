def solution(s):
    answer = []
    sample_dict = dict()
    
    for i in s:
        if i not in sample_dict.keys():
            sample_dict.update({i: 1})
            answer.append(-1)
        else:
            answer.append(sample_dict[i])
            sample_dict.update({i: 1})
        
        for key, value in sample_dict.items():
            if key != i:
                sample_dict.update({key:value+1})

    return answer