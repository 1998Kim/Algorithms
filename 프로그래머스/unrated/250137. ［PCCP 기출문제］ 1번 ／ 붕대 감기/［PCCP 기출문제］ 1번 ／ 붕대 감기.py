def solution(bandage, health, attacks):
    answer = 0
    answer += health
    
    skill_time = bandage[0]
    skill_sec = bandage[1]
    skill_plus = bandage[2]
    
    attack_time = attacks[0][0]
    attack_dam = attacks[0][1]
    del attacks[0]
    play_time = attacks[-1][0]
    # print(play_time)
    
    time = 1
    for now in range(1, play_time+1):
        if now == attack_time:
            time = 0
            answer -= attack_dam
            attack_time = attacks[0][0]
            attack_dam = attacks[0][1]
            if len(attacks) > 1:
                del attacks[0]
        else:
            time += 1
            answer += skill_sec
            if time == skill_time:
                time = 0
                answer += skill_plus
            if answer >= health:
                answer = health
        if answer <= 0:
            answer = -1
            break
    return answer