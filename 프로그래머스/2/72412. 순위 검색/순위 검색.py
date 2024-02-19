def solution(info, query):
    answer = []
    
    info_dict = {}
    for language in ['cpp', 'java', 'python', '-']:
        for work in ['backend', 'frontend', '-']:
            for carrer in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    info_dict[language + '/' + work + '/' + carrer + '/' + food] = []
    for temp in info:
        temp = temp.split()
        for language in [temp[0], '-']:
            for work in [temp[1], '-']:
                for carrer in [temp[2], '-']:
                    for food in [temp[3], '-']:
                        info_dict[language + '/' + work + '/' + carrer + '/' + food].append(int(temp[4]))
    
    for key in info_dict.keys():
        info_dict[key].sort()    
    
    for que in query:
        que = que.replace(' and ', '/').split(' ')
        condition = que[0]
        que_score = int(que[-1])

        info_scores = info_dict[condition]
        
        left_index, right_index = 0, len(info_scores) - 1
        tmp_index = len(info_scores)
        
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            
            if que_score <= info_scores[mid_index]:
                tmp_index = mid_index
                right_index = mid_index - 1
            elif que_score > info_scores[mid_index]:
                left_index = mid_index + 1
            
        answer.append(len(info_scores) - tmp_index)
    return answer