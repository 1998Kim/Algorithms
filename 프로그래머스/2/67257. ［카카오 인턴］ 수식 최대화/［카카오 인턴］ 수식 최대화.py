from itertools import permutations

def solution(expression):
    answer = 0
    
    operator = []
    if expression.find('+') != -1:
        operator.append('+')
    if expression.find('-') != -1:
        operator.append('-')
    if expression.find('*') != -1:
        operator.append('*')
    
    prioritys = list(permutations(operator, len(operator)))
    exp_num, exp_op = [], []
    temp = ''
    for s in expression:
        if s == '+' or s == '-' or s == '*':
            if temp != '':
                exp_num.append(int(temp))
                temp = ''
            exp_op.append(s)
        else:
            temp += s
    exp_num.append(int(temp))

    for priority in prioritys:
        temp_num = exp_num.copy()
        temp_op = exp_op.copy()
        for now_op in priority:
            while now_op in temp_op:
                index = temp_op.index(now_op)
                
                if now_op == '+':
                    temp_num[index] = temp_num[index] + temp_num[index+1]
                elif now_op == '-':
                    temp_num[index] = temp_num[index] - temp_num[index+1]
                elif now_op == '*':
                    temp_num[index] = temp_num[index] * temp_num[index+1]
                
                del temp_op[index]
                del temp_num[index+1]
        
        if abs(temp_num[0]) > answer:
            answer = abs(temp_num[0])
    return answer