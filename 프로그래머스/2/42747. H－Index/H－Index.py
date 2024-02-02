def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for index in range(len(citations)):
        if citations[index] >= (index+1):
            answer = index + 1
    return answer