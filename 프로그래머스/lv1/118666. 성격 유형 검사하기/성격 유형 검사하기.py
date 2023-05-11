# (R, T) (C, F), (J, M), (A, N)

def solution(survey, choices):
    keys = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    answer = ''
    
    num_dict = dict.fromkeys(keys, 0)
    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    
    for i in range(len(survey)):
        f = survey[i][0]
        b = survey[i][1]
        if choices[i] < 4:
            num_dict[f] += score[choices[i]]
        elif choices[i] > 4:
            num_dict[b] += score[choices[i]]
    
    if num_dict['R'] >= num_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    if num_dict['C'] >= num_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    if num_dict['J'] >= num_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    if num_dict['A'] >= num_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer