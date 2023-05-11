def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    score_dict = dict(zip(name, yearning))
    
    for index, peoples in enumerate(photo):
        for people in peoples:
            if people in score_dict.keys():
                answer[index] += score_dict[people]
            # else:
            #     print(people)
            # print(score_dict[people])
            # answer[index] += score_dict[people]
    
    return answer