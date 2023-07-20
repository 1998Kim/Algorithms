def solution(arr1, arr2):
    answer = []
    m = len(arr1)
    n = len(arr1[0]) # len(arr2)
    p = len(arr2[0])

    for idm in range(m):
        temp = []
        for idp in range(p):
            num = 0
            for idn in range(n):
                num += arr1[idm][idn] * arr2[idn][idp]
            temp.append(num)
        answer.append(temp)
    return answer