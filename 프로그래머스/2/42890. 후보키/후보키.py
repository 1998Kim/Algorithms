from itertools import combinations

def solution(relation):
    answer = []
    column = len(relation[0])
    row = len(relation)
    
    column_list = [i for i in range(column)]
    combs = []
    for i in range(1, column+1):
        combs += list(combinations(column_list, i))
    
    for comb in combs:
        temp = [''] * row
        for y in range(row):
            for index in comb:
                temp[y] += relation[y][index]
        
        if len(set(temp)) == row:
            min_state = True
            for x in answer:
                if set(x).issubset(comb):
                    min_state = False
                    break
            if min_state:
                answer.append(comb)
    
    return len(answer)