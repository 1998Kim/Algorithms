def solution(lottos, win_nums):
    # key는 맞힌 수, value는 등수
    win_dict = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    cnt_zero = 0
    cnt_win = 0
    for i in lottos:
        if i in win_nums:
            cnt_win +=1
        elif i == 0:
            cnt_zero += 1
            
    answer = [win_dict[cnt_win+cnt_zero], win_dict[cnt_win]]
    return answer