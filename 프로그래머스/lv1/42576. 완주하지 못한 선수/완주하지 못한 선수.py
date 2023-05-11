def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    finish = True
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            finish = False
            break
    if finish:
        answer = participant[-1]
    return answer