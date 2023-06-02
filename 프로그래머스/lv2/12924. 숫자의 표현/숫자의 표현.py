def solution(n):
    answer = 0
    for start in range(1, n+1):
        sum_num = 0
        for next_num in range(start, n+1):
            sum_num += next_num
            if sum_num == n:
                answer += 1
                break
            elif sum_num > n:
                break
    return answer