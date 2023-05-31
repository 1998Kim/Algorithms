# 효율성 문제로 인해서 DP로 풀어야함
def solution(board):
    answer = 0
    
    x = len(board[0])
    y = len(board)
    # print(x, y)
    
    dp = [[0] * x for _ in range(y)] # board와 동일한 사이즈
    # print(dp)
    for idx in range(x):
        dp[0][idx] = board[0][idx]
    for idy in range(y):
        dp[idy][0] = board[idy][0]
    # print(dp)
    
    # 변의 길이 계산
    for idx in range(1, x):
        for idy in range(1, y):
            if board[idy][idx] == 1:
                dp[idy][idx] = min(dp[idy-1][idx-1], dp[idy-1][idx], dp[idy][idx-1])+1
    # print(dp)
    
    for idy in range(y):
        now = max(dp[idy])
        answer = max(now, answer)
    # print(answer)
    return answer**2