def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        temp = list(s)
        
        stack = []
        state = True
        
        while len(temp):
            now = temp.pop(0)
        
            if now in ['(', '{', '[']:
                stack.append(now)
            elif len(stack) != 0 and now == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) != 0 and now == '}' and stack[-1] == '{':
                stack.pop()
            elif len(stack) != 0 and now == ']' and stack[-1] == '[':
                stack.pop()
            else:
                state = False
                break
                
        if state and len(stack) == 0:
            answer += 1
        
        s = s[1:] + s[0]
    
    return answer