def solution(board, h, w):
    answer = 0
    color = board[h][w]
    height = len(board)
    weight = len(board[0])
    
    if w-1 >= 0 and board[h][w-1] == color:
        answer += 1
    if w+1 < weight and board[h][w+1] == color:
        answer += 1
    if h-1 >= 0 and board[h-1][w] == color:
        answer += 1
    if h+1 < height and board[h+1][w] == color:
        answer += 1
    return answer