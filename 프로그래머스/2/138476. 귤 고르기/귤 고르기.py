from itertools import combinations
from collections import Counter

# def solution(k, tangerine):
#     answer = 0
#     stocks = Counter(tangerine)
#     state = False

#     for num in range(1, len(stocks.keys())+1):
#         if state:
#             break
#         combs = list(combinations(stocks.keys(), num))
#         for comb in combs:
#             temp = 0
#             for kind in comb:
#                 temp += stocks[kind]
#             if temp >= k:
#                 state = True
#                 answer = num
#     return answer

def solution(k, tangerine):
    answer = 0
    stocks = Counter(tangerine)
    values = sorted(stocks.values(), reverse=True)
    num = 0
    
    for i in range(len(values)):
        num += values[i]
        answer += 1
        if num >= k:
            break
    return answer