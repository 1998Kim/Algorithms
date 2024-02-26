from itertools import permutations

def solution(k, dungeons):
    answer = -1
    index_list = [i for i in range(len(dungeons))]
    orders = list(permutations(index_list, len(dungeons)))
    
    for order in orders:
        temp = k
        i = 0
        cnt = 0
    
        while order:
            if i == len(order):
                break

            index = order[i]
            if temp >= dungeons[index][0]:
                temp -= dungeons[index][1]
                cnt += 1
                i += 1
            else:
                break

        answer = max(answer, cnt)
    return answer