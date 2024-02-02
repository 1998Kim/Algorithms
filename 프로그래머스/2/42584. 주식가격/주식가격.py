def solution(prices):
    answer = []
    
    for index in range(len(prices) - 1):
        time = 1
        for j in range(index+1, len(prices)-1):
            if prices[j] < prices[index]:
                break
            time += 1
        answer.append(time)
    answer.append(0)
    return answer