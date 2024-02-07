def solution(progresses, speeds):
    answer = []
    time = 1
    work = 0
    
    while len(progresses) != 0:
        if progresses[0] + time * speeds[0] >= 100:
            del progresses[0]
            del speeds[0]
            work += 1
        else:
            time += 1
            if work != 0:
                answer.append(work)
                work = 0
    answer.append(work)
    
    return answer