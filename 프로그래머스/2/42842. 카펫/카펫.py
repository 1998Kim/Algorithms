def solution(brown, yellow):
    answer = []
    total = brown+yellow
    
    for i in range(2, int(total**(1/2))+1):
        if total % i == 0:
            x, y = total // i, i
            if (x-2) * (y-2) == yellow:
                answer.append(x)
                answer.append(y)

    return answer