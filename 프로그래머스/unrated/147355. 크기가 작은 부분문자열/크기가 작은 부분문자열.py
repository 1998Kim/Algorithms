# t에서 p와 길이가 같은 부분문자열 중 p보다 작거나 같은 것의 수
def solution(t, p):
    answer = 0
    p_num = int(p)
    
    for i in range(len(t) - len(p) + 1):
        now_int = int(t[i:i+len(p)])
        if now_int <= p_num:
            answer += 1
    return answer