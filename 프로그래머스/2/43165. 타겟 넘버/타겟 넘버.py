# BFS
# def solution(numbers, target):
#     answer = 0
#     results = [0]
    
#     for num in numbers:
#         temp = []
        
#         for result in results:
#             temp.append(result + num)
#             temp.append(result - num)
            
#         results = temp
        
#     for result in results:
#         if result == target:
#             answer += 1
    
#     return answer

# DFS
answer = 0

def dfs(numbers, target, depth, value):
    global answer

    if depth == len(numbers):
        if value == target:
            answer += 1
        return

    dfs(numbers, target, depth +1, value + numbers[depth])
    dfs(numbers, target, depth +1, value - numbers[depth])

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer
