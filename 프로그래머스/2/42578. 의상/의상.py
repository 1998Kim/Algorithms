from itertools import combinations

def solution(clothes):
    answer = 1
    clothes_dict = {}
    for name, kind in clothes:
        if kind in clothes_dict.keys():
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    
    for name in clothes_dict.keys():
        answer = answer * (clothes_dict[name] + 1)
    
    
    return answer-1