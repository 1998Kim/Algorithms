def solution(rows, columns, queries):
    answer = []
    
    board = [[y*columns + x for x in range(1, columns+1)] for y in range(rows)]
    
    for turn in range(len(queries)):
        y1, x1, y2, x2 = queries[turn]
        w, h = x2 - x1 + 1, y2 - y1 + 1
        
        dir_y, dir_x = True, True
        y, x = y1-1, x1-1
        temp = []
        for _ in range(2*(w+h)-4):
            temp.append(board[y][x])
            
            if (x == x2-1 and dir_x) or (x == x1-1 and not dir_x):
                dir_x = not dir_x
            if (y == y2-1 and dir_y):
                dir_y = not dir_y
    
            if dir_x == True and dir_y == True:
                x += 1
            elif dir_x == False and dir_y == True:
                y += 1
            elif dir_x == False and dir_y == False:
                x -= 1
            elif dir_x == True and dir_y == False:
                y -= 1
    
        answer.append(min(temp))   
        
        if turn != len(queries) - 1:
            temp = [temp[-1]] + temp[:-1]
            dir_y, dir_x = True, True
            y, x = y1-1, x1-1
            
            for _ in range(2*(w+h)-4):
                board[y][x] = temp.pop(0)

                if (x == x2-1 and dir_x) or (x == x1-1 and not dir_x):
                    dir_x = not dir_x
                if (y == y2-1 and dir_y):
                    dir_y = not dir_y

                if dir_x == True and dir_y == True:
                    x += 1
                elif dir_x == False and dir_y == True:
                    y += 1
                elif dir_x == False and dir_y == False:
                    x -= 1
                elif dir_x == True and dir_y == False:
                    y -= 1
            
    return answer