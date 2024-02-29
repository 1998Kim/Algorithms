# def solution(topping):
#     answer = 0
    
#     for index in range(1, len(topping)):
#         temp1 = set(topping[:index])
#         temp2 = set(topping[index:])
#         if len(temp1) == len(temp2):
#             answer += 1

#     return answer
from collections import Counter


def solution(topping):
    answer = 0
    up = Counter(topping)
    down = set()
    
    for t in topping:
        up[t] -= 1
        down.add(t)
        
        if up[t] == 0:
            up.pop(t)

        if len(up.keys()) == len(down):
            answer += 1
    return answer