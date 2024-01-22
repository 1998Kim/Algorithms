global answer, visit
answer = 0

def check(queen_coord, new):
    for index in range(len(queen_coord)):
        if queen_coord[index] == new or abs(new - queen_coord[index]) == abs(len(queen_coord) - index): # 가로세로 / 대각선 확인
            return False
    return True

def position(queen_coord, queen_num, visit):
    global answer
    if len(queen_coord) == queen_num: # 조건 성립
        answer += 1
        return 
    
    for i in range(queen_num):
        if visit[i]:
            continue
        
        if check(queen_coord, i):
            visit[i] = True
            position(queen_coord+[i], queen_num, visit)
            visit[i] = False

    return 

def solution(n):
    visit = [False] * n
    position([], n, visit)
    return answer
