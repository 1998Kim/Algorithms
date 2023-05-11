# keymap은 1번 키부터 할당된 문자들
# target는 적을 문자
def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        target_state = True
        for target_str in target:
            press_key = []
            for keys in keymap:
                index = keys.find(target_str)
                if index != -1:
                    press_key.append(index + 1)
            if len(press_key) == 0:
                target_state = False
    
            if target_state:
                # print(cnt, target_str, press_key)
                cnt += min(press_key)
            else:
                answer.append(-1)
                break
                # print(target, target_str, keys, keys.find(target_str))
        if target_state:
            answer.append(cnt)
    
    return answer