from itertools import combinations

def solution(number):
    answer = 0
    sample_list = combinations(number, 3)
    for i in sample_list:
        if sum(i) == 0:
            answer += 1
    return answer