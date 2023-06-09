# DP 풀이
def solution(n):
    answer = [0, 1]
    for idx in range(2, n+1):
        answer.append((answer[idx-2] + answer[idx-1]) % 1234567)
    return answer[-1]

# 재귀함수 풀이
# def factorial(n):
#     pass

# def solution(n):
#     answer = 0
#     return answer