def solution(food):
    answer = ''
    temp = ''
    
    for index, value in enumerate(food):
        if index != 0:
            temp += str(index) * (value // 2)
    
    temp_list = list(temp)
    reverse_temp = ''.join(list(reversed(temp_list)))
    answer = temp + '0' + reverse_temp    
    return answer