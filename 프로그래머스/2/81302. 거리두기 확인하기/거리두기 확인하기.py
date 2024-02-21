def solution(places):
    answer = []
    
    for place in places:
        place = [list(line) for line in place]
        check = True
        
        for y in range(5):
            if check == False:
                break
            
            for x in range(5):
                if place[y][x] == 'P':
                    if x + 1 < 5:
                        if place[y][x + 1] == 'P':
                            check = False
                        elif place[y][x + 1] == 'O' and (x + 2 < 5 and place[y][x + 2] == 'P'):
                            check = False
                    if y + 1 < 5:
                        if place[y+1][x] == 'P':
                            check = False
                        elif place[y+1][x] == 'O' and (y + 2 < 5 and place[y+2][x] == 'P'):
                            check = False
                    
                    if x + 1 < 5 and y - 1 >= 0:
                        if place[y-1][x+1] == 'P' and (place[y][x+1] == 'O' or place[y-1][x] == 'O'):
                            check = False
                    if x + 1 < 5 and y + 1 < 5:
                        if place[y+1][x+1] == 'P' and (place[y][x+1] == 'O' or place[y+1][x] == 'O'):
                            check = False
        if check == True:
            answer.append(1)
        else:
            answer.append(0)
    return answer