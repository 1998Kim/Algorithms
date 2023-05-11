def solution(board, moves):
    answer = 0
    result = []
    n = len(board)
    
    for i in moves:
        index = i-1
        for j in range(n):
            print(i, index, j, board[j][index])
            if board[j][index] != 0:
                result.append(board[j][index])
                board[j][index] = 0
                break
        if len(result) >= 2:
            if result[-2] == result[-1]:
                result.pop(-2)
                result.pop(-1)
                answer += 2

    return answer