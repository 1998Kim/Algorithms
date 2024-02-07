def solution(priorities, location):
    answer = 0
    new = priorities.copy()
    new[location] = str(new[location])

    while True:
        now = new.pop(0)
        
        if int(now) == max(priorities):
            answer += 1
            if type(now) == str:
                break
            else:
                del priorities[priorities.index(max(priorities))]
        else:
            new.append(now)

    return answer