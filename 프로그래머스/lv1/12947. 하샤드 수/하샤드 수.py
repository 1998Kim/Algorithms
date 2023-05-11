def solution(x):
    answer = True
    str_x = str(x)
    dev_x = 0
    for i in str_x:
        dev_x += int(i)
    if x % dev_x != 0:
        answer = False
    
    return answer