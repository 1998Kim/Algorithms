def solution(park, routes):
    W, H = len(park[0]), len(park)
    for line_index, line in enumerate(park):
        check = False
        for pt_index, pt in enumerate(line):
            if pt == 'S':
                start_x = pt_index
                start_y = line_index
                state = True
        if check:
            break
    
    for rout in routes:
        direction, cnt = rout.split()
        cnt = int(cnt)
        # print('now y, x', start_y, start_x)
        
        if direction == 'E':
            if start_x + cnt < W:
                if 'X' not in park[start_y][start_x+1: start_x + cnt + 1]:
                    start_x += cnt
            #         print('E 이동가능 이동함')
            #     else:
            #         print('E 이동가능 but 장애물')
            # else:
            #     print('E 이동불가')
        elif direction == 'W':
            if start_x - cnt >= 0:
                if 'X' not in park[start_y][start_x - cnt: start_x]:
                    start_x -= cnt
            #         print('W 이동가능 이동함')
            #     else:
            #         print('W 이동가능 but 장애물')
            # else:
            #     print('W 이동불가')
        elif direction == 'S':
            if start_y + cnt < H:
                loads = park[start_y + 1: start_y + cnt + 1]
                y_state = True
                for load in loads:
                    if load[start_x] == 'X':
                        y_state = False
                    if y_state == False:
                        break
                if y_state:
                    start_y += cnt
            #         print('S 이동가능 이동함')
            #     else:
            #         print('S 이동가능 but 장애물')
            # else:
            #     print('S 이동불가')
        elif direction == 'N':
            if start_y - cnt >= 0:
                loads = park[start_y - cnt: start_y]
                y_state = True
                for load in loads:
                    if load[start_x] == 'X':
                        y_state = False
                    if y_state == False:
                        break
                if y_state:
                    start_y -= cnt
            #         print('N 이동가능 이동함')
            #     else:
            #         print('N 이동가능 but 장애물')
            # else:
            #     print('N 이동불가')
        

    # print('finish y, x', start_y, start_x)
    answer = [start_y, start_x]
    return answer