def change(n, number):
    n_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
              10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    temp = ''
    
    while True:
        if number // n == 0:
            temp += n_dict[number]
            break
        temp += n_dict[number % n]
        number = number // n
        
    return temp[::-1]

def solution(n, t, m, p):
    answer = ''

    num = 0
    total_answer = ''
    while True:
        num_n = change(n, num)
        num += 1
        total_answer += num_n
        if len(total_answer) // m == t:
            break

    for i in range(p-1, len(total_answer), m):
        answer += total_answer[i]
        if len(answer) == t:
            break
    return answer