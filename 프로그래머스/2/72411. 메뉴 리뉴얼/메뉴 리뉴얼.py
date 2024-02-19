# 시간 초과
# from itertools import combinations

# def solution(orders, course):
#     answer = []
#     alpha = [chr(x) for x in range(ord('A'), ord('Z')+1)]
#     orders_max_num = max([len(order) for order in orders])

#     for num in course:
#         if num > orders_max_num:
#             break
#         combs = list(combinations(alpha, num))
#         menus = []
#         order_num = 2
        
#         for comb in combs:
#             num = 0
#             for order in orders:
#                 state = True
#                 for menu in comb:
#                     if menu not in order:
#                         state = False
#                         break
#                 if state:
#                     num += 1
#             if num > order_num:
#                 order_num = num
#                 menus = [''.join(comb)]
#             elif num == order_num:
#                 menus.append(''.join(comb))
#         answer += menus
    
#     return sorted(answer)

from itertools import combinations

def solution(orders, course):
    answer = [] 
    
    combs = []
    for order in orders:
        for course_num in course:
            combs += list(combinations(sorted(order), course_num))
    
    menus = {course_num: {'order_num': 2, 'menus': []} for course_num in course}
    for comb in combs:
        order_num = 0
        for order in orders:
            state = True
            for menu in comb:
                if menu not in order:
                    state = False
                    break
            if state:
                order_num += 1
        
        if menus[len(comb)]['order_num'] == order_num:
            if ''.join(comb) not in menus[len(comb)]['menus']:
                menus[len(comb)]['menus'].append(''.join(comb))
        elif menus[len(comb)]['order_num'] < order_num:
            menus[len(comb)]['order_num'] = order_num
            menus[len(comb)]['menus'] = [''.join(comb)]   
    
    for values in menus.values():
        if len(values['menus']) != 0:
            answer += values['menus']
    return sorted(answer)