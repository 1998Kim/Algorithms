def solution(files):
    answer = []
    
    for file in files:
        # head, number, tail로 구분
        num_state = False
        head = ''
        number = ''
        for s in file:
            if s.isdigit():
                number += s
                num_state = True
            elif num_state == False:
                head += s
            else:
                break
                
                
        answer.append([head, number, file])

    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    answer = [ans[2] for ans in answer]
        
    return answer