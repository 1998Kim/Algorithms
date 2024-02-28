def solution(elements):
    answer = 0
    cycle = elements * 2
    case = set()
    
    for index in range(len(elements)):
        for length in range(1, len(elements)+1):
            temp = cycle[index:index+length]
            case.add(sum(temp))
    answer = len(case)
    return answer