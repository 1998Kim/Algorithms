def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 11]]
    lpos = 10
    rpos = 11
    # print(len(keypad))    # 4 : y방향
    # print(len(keypad[0])) # 3 : x방향

    for number in numbers:
        if number in (1,4,7): # 무조건 왼쪽으로 누르는 경우
            lpos = number
            answer += 'L'
        elif number in (3, 6, 9): # 무조건 오른쪽으로 누르는 경우
            rpos = number
            answer += 'R'
        else:
            target_x, target_y, left_x, left_y, right_x, right_y = 0,0,0,0,0,0
            for i in range(len(keypad[0])):  # x방향
                for j in range(len(keypad)): # y방향
                    if keypad[j][i] == number:
                        target_x = i
                        target_y = j
                    if keypad[j][i] == lpos:
                        left_x = i
                        left_y = j
                    if keypad[j][i] == rpos:
                        right_x = i
                        right_y = j
            dis_r = abs(right_x - target_x) + abs(right_y - target_y)
            dis_l = abs(left_x - target_x) + abs(left_y - target_y)

            if dis_l < dis_r:
                lpos = number
                answer += 'L'
            elif dis_l > dis_r:
                rpos = number
                answer += 'R'
            elif dis_l == dis_r:
                if hand == 'right':
                    rpos = number
                    answer += 'R'
                else:
                    lpos = number
                    answer += 'L'
    return answer