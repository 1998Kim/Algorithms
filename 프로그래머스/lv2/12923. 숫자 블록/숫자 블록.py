def solution(begin, end):
    answer = []
    for num in range(begin, end+1):
        if num == 1:
            answer.append(0)
        else:
            min_num = 1
            state = True # 최대 약수를 구했는데 10,000,000이상인 경우 확인
            for i in range(2, int(num**(1/2)) + 1):
                if num % i == 0:
                    if num // i <= 10000000:
                        state = False
                        answer.append(num // i)
                        break
                    else:
                        min_num = i
            if state:
                answer.append(min_num)
    return answer