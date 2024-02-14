# def solution(w,h):
#     answer = 0
    
#     for W in range(1, w):
#         H = h * W / w
#         answer += int(H)
    
#     return answer*2

def max_divide(a, b):
    for index in range(min(a, b), 0, -1):
        if a % index == 0 and b % index == 0:
            return index

def solution(w,h):
    max_divide_num = max_divide(w, h)
    
    answer = w*h - (w+h-max_divide_num)
    
    return answer