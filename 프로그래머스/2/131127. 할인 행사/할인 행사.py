def solution(want, number, discount):
    answer = 0
    
    for index in range(len(discount)-9):
        temp = discount[index:index+10]
        state = True
        member_state = True

        for now in want:
            if now not in temp:
                state = False
                break

        if state:
            for i, name in enumerate(want):
                if temp.count(name) != number[i]:
                    member_state = False

            if member_state:
                answer += 1
    
    return answer