# 사과점수 : 1~k
# 한 상자 포장 갯수 : m
# 사과 한 상자의 가격 : p * m 단, p는 상자에 담긴 사과중 최하점

def solution(k, m, score):
    answer = 0
    apple = [score.count(i+1) for i in range(k)]  # index + 1의 점수를 갖는 사과 갯수
    
    # 알고리즘은 맞으나 시간초과
    # while len(score) >= m:
    #     now = score[-m:]
    #     score = score[:-m]
    #     answer += min(now) * m
    
    for i in range(k-1, -1, -1):
        cnt, rest = divmod(apple[i], m) # cnt는 상자 갯수, rest는 상자 만들고 남은 사과 갯수
        if i != 0:
            apple[i-1] += rest
        answer += (i+1) * m * cnt
    
    return answer