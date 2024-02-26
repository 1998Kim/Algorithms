import math

def solution(fees, records):
    answer = []
    records_dict = {}
    
    for record in records:
        time, number, state = record.split(' ')
        
        if number not in records_dict.keys():
            records_dict[number] = {'IN': [time], 'OUT': []}
        elif state == 'OUT':
            records_dict[number]['OUT'].append(time)
        elif state == 'IN':
            records_dict[number]['IN'].append(time)
    
    records_dict = dict(sorted(records_dict.items()))

    for info in records_dict.values():
        in_list, out_list = info['IN'], info['OUT']
        time = 0
        
        for index in range(len(in_list)):
            in_hour, in_min = in_list[index].split(':')
            if index == len(out_list):
                out_hour, out_min = '23', '59'
            else:
                out_hour, out_min = out_list[index].split(':')
            time += (int(out_hour)*60 + int(out_min)) - (int(in_hour)*60 + int(in_min))
        
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((time - fees[0]) / fees[2])*fees[3])
        
    return answer