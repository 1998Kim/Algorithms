def solution(players, callings):
    # 리스트 형식은 시간초과 떠서 딕셔너리 형식으로 해야함
    # 알고리즘은 맞으나 시간초과
    # for now in callings:
    #     now_index = players.index(now)
    #     before_people = players[now_index - 1]
    #     players[now_index - 1] = now
    #     players[now_index] = before_people
    
    score_dict = {index: player for index, player in enumerate(players)}
    score_invert = {player: index for index, player in enumerate(players)}
    # print(score_dict)
    # print(score_invert)
    
    for now_name in callings:
        now_score = score_invert[now_name]
        front_score = now_score - 1
        front_name = score_dict[front_score]
        
        score_dict[front_score] = now_name
        score_dict[now_score] = front_name
        
        score_invert[front_name] = now_score
        score_invert[now_name] = front_score
        # print(now_name, now_score, front_name, front_score)
    
    # print(list(score_dict.values()))
    
    return list(score_dict.values())