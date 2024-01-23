def solution(s):
    stack = []
    
    for alpha in s:
        if len(stack) == 0:
            stack.append(alpha)
        elif stack[-1] == alpha:
            stack.pop()
        else:
            stack.append(alpha)

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
            
    return answer