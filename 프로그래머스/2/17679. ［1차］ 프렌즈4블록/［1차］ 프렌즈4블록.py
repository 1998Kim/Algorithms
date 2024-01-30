def solution(m, n, board):
    answer = 0
    
    while True:
        check = [[False] * n for _ in range(m)]
        coord = set()
        
        for y in range(m-1, 0, -1):
            for x in range(n-1):
                if board[y][x] == board[y][x+1] == board[y-1][x] == board[y-1][x+1] != 'X':
                    coord.update([(x, y), (x+1, y), (x, y-1), (x+1, y-1)])
                    check[y][x], check[y][x+1], check[y-1][x], check[y-1][x+1] = True, True, True, True
        
        for y in range(m-1, -1, -1):
            for x in range(n):
                if check[y][x]:
                    change_state = False
                    for new_y in range(y-2, -1, -1):
                        if board[new_y][x] != 'X' and check[new_y][x] == False:
                            check[new_y][x] = True
                            change_state = True
                            break
                    
                    if change_state:
                        board[y] = board[y][:x] + board[new_y][x]+ board[y][x+1:]
                        board[new_y] = board[new_y][:x] + 'X' + board[new_y][x+1:]
                    else:
                        board[y] = board[y][:x] + 'X' + board[y][x+1:]
        if len(coord) == 0:
            break
        answer += len(coord)
    return answer
