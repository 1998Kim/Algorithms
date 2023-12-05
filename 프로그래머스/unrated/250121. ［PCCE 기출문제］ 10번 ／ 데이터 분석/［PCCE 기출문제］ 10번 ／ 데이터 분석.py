def solution(data, ext, val_ext, sort_by):
    data_index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    find_index = data_index[ext]
    sort_index = data_index[sort_by]
    answer = []
    
    for i in range(len(data)):
        if data[i][find_index] < val_ext:
            answer.append(data[i])
    answer.sort(key=lambda x: x[sort_index])        
    return answer