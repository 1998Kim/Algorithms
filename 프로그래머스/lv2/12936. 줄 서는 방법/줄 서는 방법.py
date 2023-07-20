# 시간초과 풀이
# from itertools import permutations
# def solution(n, k):
#     members = [i for i in range(1, n+1)]
#     answer = list(permutations(members, len(members)))[k-1]
#     return answer
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def solution(n, k):
    answer = []
    people = [i+1 for i in range(n)]
    print('people: ', people)
    while (n != 0):
        now = factorial(n-1)
        rest = k % now
        if rest != 0:
            index = k // now
        else:
            index = (k // now) - 1
        # answer.append(people[index])
        answer.append(people[index])
        del people[index]
        n -= 1
        k = rest
    return answer