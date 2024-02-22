# 시간초과
# def solution(n, left, right):
#     answer = []
#     graph = [[num+1 for num in range(n)] for _ in range(n)]

#     for j in range(1, n+1):
#         for i in range(j):
#             graph[j-1][i] = j
            
#     for temp in graph:
#         answer += temp

#     return answer[left:right+1]

def solution(n, left, right):
    answer = []
    for num in range(left, right+1):
        answer.append(max(num//n, num%n)+1)
    return answer