from itertools import product

def solution(word):
    answer = 0
    pros = []
    for num in range(1, 6):
        temp = list(product(['A', 'E', 'I', 'O', 'U'], repeat=num))
        pros += [''.join(words) for words in temp]
    
    pros.sort()
    answer = pros.index(word) + 1
    
    return answer