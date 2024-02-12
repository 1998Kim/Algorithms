def solution(dirs):
    answer = set()
    now_x, now_y = 0, 0
    direction = {"U": (0,1), "D": (0,-1), "R": (1,0), "L": (-1,0)}
    
    for d in dirs:
        dir_x, dir_y = direction[d]
        next_x = now_x + dir_x 
        next_y = now_y + dir_y
    
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            answer.add((now_x, now_y, next_x, next_y))
            answer.add((next_x, next_y, now_x, now_y))
            now_x = next_x
            now_y = next_y
    
    return len(answer) // 2