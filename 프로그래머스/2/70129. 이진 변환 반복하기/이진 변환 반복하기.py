def solution(s):
    cnt, num_zero = 0, 0

    while s != '1':
        cnt += 1
        temp = ''
        for i in s:
            if i == '0':
                num_zero += 1
            else:
                temp += i
        s = bin(len(temp))[2:]

    answer = [cnt, num_zero]

    return answer