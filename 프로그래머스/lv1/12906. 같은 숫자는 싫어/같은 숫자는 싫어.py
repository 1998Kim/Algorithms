def solution(arr):
    answer = [arr[0]]
    index = 0
    
    for i in range(1, len(arr)):
        if arr[i] == answer[index]:
            continue
        else:
            index += 1
            answer.append(arr[i])
    return answer