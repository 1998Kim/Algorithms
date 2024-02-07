def solution(priorities, location):
    answer = 0
    new = priorities.copy()
    new[location] = str(new[location])

    while True:
        now = new.pop(0)
        
        if int(now) >= max(priorities):
            if type(now) == str:
                answer += 1
                break
            else:
                del priorities[priorities.index(max(priorities))]
                answer += 1
        else:
            new.append(now)

    return answer