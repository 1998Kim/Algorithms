def solution(n, arr1, arr2):
    answer = []
    # print(bin(9)[2:].zfill(n))
    
    for i in range(n):
        temp = ''
        arr1_str = bin(arr1[i])[2:].zfill(n)
        arr2_str = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if arr1_str[j] == '1' or arr2_str[j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer