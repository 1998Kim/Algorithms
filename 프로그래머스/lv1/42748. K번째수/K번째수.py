def solution(array, commands):
    answer = []
    for now_list in commands:
        i, j, k = now_list[0], now_list[1], now_list[2]
        now_array = array[i - 1:j]
        now_array.sort()
        answer.append(now_array[k-1])
    
    return answer