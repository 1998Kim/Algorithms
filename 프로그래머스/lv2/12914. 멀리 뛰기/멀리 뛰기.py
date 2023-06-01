# 알고리즘은 맞는 것 같은데 시간초과가 나옴
# from itertools import permutations
# from collections import deque
# def solution(n):
#     answer = 0
#     if n < 3: # 1칸 혹은 2칸 뛸 경우 생각할 필요 X
#         answer = n
#     else:
#         Queue = deque([1 for _ in range(n)])
#         while True:
#             if Queue[1] == 2: # 더 이상 조합이 나올 수 없는 경우까지 확인함
#                 answer += len(set(permutations(Queue, len(Queue)))) % 1234567
#                 break
#             else:
#                 answer += len(set(permutations(Queue, len(Queue)))) % 1234567
#                 Queue.popleft()
#                 Queue.popleft()
#                 Queue.append(2)
#     return answer

# DP로 풀어야 하는 듯
# 점화식 : f(n) = f(n-1) + f(n-2)
def solution(n):
    if n < 4:
        answer = [i+1 for i in range(n)]
    else:
        answer = [1, 2, 3]
        for i in range(3, n):
            answer.append((answer[i-1]+answer[i-2]) % 1234567)
    return answer[-1]