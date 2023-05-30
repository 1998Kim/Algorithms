# n = 1,2,3 --- 일 때 수 계산해보기
def solution(n):
    answer = 0
    if n < 3:
        answer = n
    else:
        answer = [1, 2]
        for i in range(2, n):
            # print(len(answer), i-1, i-2)
            answer.append((answer[i-1] + answer[i-2])%1000000007)
    # print(answer)    
    return answer[-1]