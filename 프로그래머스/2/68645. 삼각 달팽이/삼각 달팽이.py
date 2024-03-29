# 메모리: 43.2 MB, 시간: 129.49 ms
# def solution(n):
#     answer = []
#     temp = [[0] * i for i in range(1, n+1)]
#     cnt = 1
#     floor = n
#     start, end = 0, -1

#     for i in range(n, 0, -1):
#         now = [num for num in range(cnt, cnt+i)]
#         cnt = now[-1]+1
#         state = ''   
#         for j in range(len(now)):
#             if (n-i) % 3 == 0:
#                 state = 'down'
#                 temp[(n-i)//3*2 + j][start] = now[j]
#             elif (n-i) % 3 == 2:
#                 state = 'up'
#                 temp[(n-1) - (n-i)//3 - (j+1)][end] = now[j]
#             else:
#                 y_index = (n-1) - (n-i)//3
#                 x_index = temp[(n-1) - (n-i)//3].index(0)
#                 temp[y_index][x_index:x_index+len(now)] = now
#                 break
#         if state == 'down':
#             start += 1
#         elif state == 'up':
#             end -= 1
            
#     for i in temp:
#         answer += i

#     return answer

direction = {0: (0, 1), 1: (1, 0), 2: (-1, -1)}

def solution(n):
    answer = []
    temp = [[0] * i for i in range(1, n+1)]
    x, y, num = 0, -1, 1
    
    for i in range(n):
        for _ in range(i, n):
            dir_x, dir_y = direction[i%3]
            x = x + dir_x
            y = y + dir_y
            temp[y][x] = num
            num += 1
    
    for i in temp:
        answer += i
    return answer