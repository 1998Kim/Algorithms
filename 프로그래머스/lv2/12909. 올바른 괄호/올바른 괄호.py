from collections import deque
# 시간초과
# def solution(s):
#     answer = True
#     if s[0] == ')':
#         answer = False
#     else:
#         Queue = deque()
#         Queue.append(s[0])
#         s = s[1:]
#         while s:
#             now = s[0]
#             if now == '(':
#                 Queue.append(now)
#             elif len(Queue) != 0:
#                 Queue.pop()
#             elif len(Queue) == 0:
#                 break
#             s = s[1:]
#         if len(s) == 0 and len(Queue) == 0:
#             answer = True
#         else:
#             answer = False
#     return answer
def solution(s):
    answer = True
    Queue = deque(s)
    check = 0
    while Queue:
        now = Queue.popleft()
        if now == ')':
            check -= 1
        else:
            check += 1
        if check < 0:
            break
    if check != 0:
        answer = False
    return answer