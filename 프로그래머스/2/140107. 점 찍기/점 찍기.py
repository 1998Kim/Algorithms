def solution(k, d):
    answer = 0
    x = 0
    
    while x <= d:
        max_y = int((d**2 - x**2)**(0.5))
        answer += max_y // k + 1
        x += k
    
    return answer