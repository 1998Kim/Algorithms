def solution(record):
    infos = {}
    index = 0
    
    for rec in record:
        rec_split = rec.split(' ')
        if len(rec_split) == 3:
            action, user_id, nickname = rec_split[0], rec_split[1],  rec_split[2]
        else:
            action, user_id = rec_split[0], rec_split[1], 
            
        if action == 'Enter':
            if user_id not in infos.keys():
                infos[user_id] = {'in': [index], 'out': [], 'nickname': nickname}
            else:
                infos[user_id]['nickname'] = nickname
                infos[user_id]['in'].append(index)
            index += 1
        elif action == 'Leave':
            infos[user_id]['out'].append(index)
            index += 1
        elif action == 'Change':
            infos[user_id]['nickname'] = nickname

    answer = [''] * index
    for info in infos.values():
        info_in, info_out, name = info['in'], info['out'], info['nickname']
        
        for index in range(len(info_in)):
            answer[info_in[index]] = f"{name}님이 들어왔습니다."
        
        for index in range(len(info_out)):
            answer[info_out[index]] = f"{name}님이 나갔습니다."
    return answer