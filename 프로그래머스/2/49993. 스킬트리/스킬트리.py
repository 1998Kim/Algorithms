def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        state = True
        temp = skill[:]
        
        for now in skill_tree:
            if now in temp:
                if now == temp[0]:
                    temp = temp[1:]
                else:
                    state = False
                    break
        if state:
            answer += 1

    return answer