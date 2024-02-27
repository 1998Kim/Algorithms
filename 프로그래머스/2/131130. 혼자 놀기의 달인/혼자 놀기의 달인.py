def solution(cards):
    answer = 0
    
    indexs = [False] * len(cards)
    length = []
    temp = []
    
    while True:
        if False not in indexs:
            length.append(len(temp))
            break

        if len(temp) == 0:
            index = indexs.index(False)

        now = cards[index]
        indexs[index] = True

        if now not in temp:
            temp.append(now)
        else:
            length.append(len(temp))
            temp = []

        index = now - 1    
    
    if len(length) >= 2:
        length.sort(reverse=True)
        answer = length[0] * length[1]
    
    return answer