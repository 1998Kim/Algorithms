def solution(X, Y):
    answer = ''
    # 시간 초과
    # pair = []
    # for i in X:
    #     if i in Y:
    #         pair.append(i)
    #         Y = Y.replace(i, '', 1) 
    # if len(pair) == 0:
    #     answer = '-1'
    # else:
    #     pair = list(map(int, pair))
    #     pair.sort(reverse=True)
    #     if sum(pair) == 0:
    #         answer = '0'
    #     else:
    #         pair = list(map(str, pair))
    #         answer = ''.join(pair)
    
    pair = []
    for i in range(0, 10):
        num = str(i)
        num_x = X.count(num)
        num_y = Y.count(num)
        if num_x != 0 and num_y != 0:
            pair += num * min(num_x, num_y)

    if len(pair) == 0:
        answer = '-1'
    else:
        pair = list(map(int, pair))
        pair.sort(reverse=True)
        if sum(pair) == 0:
            answer = '0'
        else:
            pair = list(map(str, pair))
            answer = ''.join(pair)
    return answer