def solution(n):
    answer = [0, 3, 11]
    
    if n % 2 == 1: # 홀수라면 가득 채울 수 없음
        return 0
    else:
        n = int(n / 2)
        if n < 3:
            return answer[n]
        else:
            for i in range(3, n+1):
                answer.append((3*answer[i-1] + 2*sum(answer[1:i-1]) + 2) % 1000000007)
    return answer[-1]