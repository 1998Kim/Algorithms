def solution(msg):
    answer = []
    keyword = {}
    
    for i in range(ord('A'), ord('Z')+1):
        keyword[chr(i)] = i - (ord('A') - 1)
    
    num = 1
    
    while True:
        w = msg[:num]
        if len(msg) - num > 0:
            c = msg[num]
        else:
            c = ''
        
        if c == '':
            answer.append(keyword[w])
            break
        check = w+c
        if check not in keyword.keys():
            answer.append(keyword[w])
            keyword[check] = len(keyword) + 1
            msg = msg[num:]
            num = 1
        else:
            num += 1
    
    return answer