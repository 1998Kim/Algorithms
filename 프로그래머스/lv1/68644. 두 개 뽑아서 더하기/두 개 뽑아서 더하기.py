from itertools import combinations

def solution(numbers):
    answer = []
    result = list(combinations(numbers, 2))
    
    for i in result:
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()
    
    return answer