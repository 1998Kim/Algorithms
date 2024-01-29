def solution(str1, str2):
    answer = 0
    
    A, B = [], []
    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            A.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            B.append(str2[i:i+2].lower())

    A_copy, B_copy = A.copy(), B.copy()
    inter, outer = [], []
    
    for el in A:
        if el in B_copy:
            inter.append(el)
            A_copy.remove(el)
            B_copy.remove(el)
            
    outer = A_copy + B_copy + inter
    
    if len(outer) == 0:
        answer = 65536
    else:
        answer = int(len(inter) / len(outer) * 65536)
    return answer