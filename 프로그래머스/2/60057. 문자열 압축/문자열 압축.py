def solution(s):
    answer = len(s)
    
    for length in range(1, len(s)):
        temp = [s[index:index+length] for index in range(0, len(s), length)]
        cnt = 1
        past = temp.pop(0)
        temp_str = ''
        
        while len(temp) > 0:
            now = temp.pop(0)
            if now != past:
                if cnt > 1:
                    temp_str += str(cnt) + past
                else:
                    temp_str += past
                cnt = 1
                past = now
            elif now == past:
                cnt += 1
            
            if len(temp) == 0:
                if cnt > 1:
                    temp_str += str(cnt) + past
                else:
                    temp_str += past
                    
        if len(temp_str) < answer:
            answer = len(temp_str)

    return answer