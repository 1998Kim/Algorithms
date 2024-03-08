import math

def div_num(array):
    temp = 0
    for num in array:
        temp = math.gcd(temp, num)
    return temp


def check(div_num, array):
    if div_num == 0:
        return 0
    else:
        for card in array:
            if card % div_num == 0:
                return 0
        return div_num

def solution(arrayA, arrayB):
    answer = 0
    arrayA, arrayB = list(set(arrayA)), list(set(arrayB))
    divA, divB = div_num(arrayA), div_num(arrayB)
    maxA, maxB = check(divA, arrayB), check(divB, arrayA)
    answer = max(maxA, maxB)

    return answer