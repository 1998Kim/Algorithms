def solution(strings, n):
    answer = []
    new_str = []
    for i in strings:
        new_str.append(i[n] + i)
    new_str.sort()
    
    for i in new_str:
        answer.append(i[1:])
    return answer