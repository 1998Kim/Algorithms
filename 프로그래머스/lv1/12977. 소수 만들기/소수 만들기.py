from itertools import combinations

def solution(nums):
    answer = 0
    result = list(combinations(nums, 3))

    for i in result:
        state = True
        for j in range(2,sum(i)):
            if sum(i) % j == 0:
                state = False
                break
        if state:
            answer += 1
    return answer