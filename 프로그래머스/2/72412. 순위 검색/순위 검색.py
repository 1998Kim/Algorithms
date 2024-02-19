def solution(info, query):
    answer = []
    
    info_dict = {}
    for language in ['cpp', 'java', 'python', '-']:
        for job in ['backend', 'frontend', '-' ]:
            for carrer in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    info_dict[language + job + carrer + food] = []
                    
    for tmp in info:
        tmp = tmp.split(' ')
        for language in [tmp[0], '-']:
            for job in [tmp[1], '-' ]:
                for carrer in [tmp[2], '-']:
                    for food in [tmp[3], '-']:
                        info_dict[language + job + carrer + food].append(int(tmp[4]))
    
    for key in info_dict.keys():
        info_dict[key].sort()
    
    for que in query:
        que = que.replace(' and ', '').split(' ')
        condition = que[0]
        score = int(que[-1])
        
        info_scores = info_dict[condition]
        left_index, right_index = 0, len(info_scores) - 1
        temp_index = len(info_scores)
        
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            
            if score <= info_scores[mid_index]:
                temp_index = mid_index
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
        
        answer.append(len(info_scores) - temp_index)
    return answer