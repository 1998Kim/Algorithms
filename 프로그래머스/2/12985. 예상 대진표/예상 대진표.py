def solution(n,a,b):
    answer = 0
    
    if a > b:
        a, b = b, a
    
    while True:
        answer += 1

        if a+1 == b and a % 2 == 1:
            break
        else:
            if a % 2 == 0:
                a = a // 2
            else:
                a = a // 2 +1
            if b % 2 == 0:
                b = b // 2
            else:
                b = b // 2 +1
    

    return answer