def solution(ingredient):
    answer = 0
    sample = []
    for i in ingredient:
        sample.append(i)
        if sample[-4:] == [1, 2, 3, 1]:
            answer += 1
            del sample[-4:]
            
    return answer