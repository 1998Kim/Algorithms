def solution(numbers):
    answer = ''
    numbers = sorted([str(num)*4 for num in numbers], reverse=True)
    answer = str(int(''.join([num[:len(num)//4] for num in numbers])))
    return answer