# DP 풀이
def solution(n):
    answer = [0, 1]
    for idx in range(2, n+1):
        answer.append((answer[idx-2] + answer[idx-1]) % 1234567)
    return answer[-1]

# 재귀함수 풀이 -> 시간초과
# def fibonachi(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         result = fibonachi(n-2) + fibonachi(n-1)
#         return result % 1234567

# def solution(n):
#     answer = fibonachi(n)
#     return answer