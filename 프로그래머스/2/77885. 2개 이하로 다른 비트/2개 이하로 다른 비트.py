# 시간초과
# def solution(numbers):
#     answer = []
    
#     for num in numbers:
#         num_bit = bin(num)[2:]
#         now = num + 1
#         while True:
#             now_bit = bin(now)[2:]
#             cnt = 0

#             if len(num_bit) != len(now_bit):
#                 num_bit = '0' * (len(now_bit) - len(num_bit)) + num_bit
            
#             for index in range(len(now_bit)):
#                 if num_bit[index] != now_bit[index]:
#                     cnt += 1
#                 if cnt == 3:
#                     break
            
#             if cnt == 1 or cnt == 2:
#                 answer.append(now)
#                 break
            
#             now += 1
            
#     return answer

def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            num_bin = bin(num)[2:]

            if num_bin.find('0') == -1:
                num_bin = '0' + num_bin
            index = num_bin.rindex('0')
            num_bin = num_bin[:index] + '10' + num_bin[index+2:]
            answer.append(int('0b' + num_bin, 2))
    return answer