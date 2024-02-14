def check(u):
    stack = []
    
    for s in u:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return True

def divide(w):
    left, right = 0, 0
    
    for index in range(len(w)):
        if w[index] == '(':
            left += 1
        elif w[index] == ')':
            right += 1
            
        if left == right:
            return w[:index+1], w[index+1:]

def solution(p):
    if p == '':
        return p
    
    answer = ''
    u, v = divide(p)
    
    if check(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        
        for index in range(1, len(u)-1):
            if u[index] == '(':
                answer += ')'
            elif u[index] == ')':
                answer += '('
    return answer