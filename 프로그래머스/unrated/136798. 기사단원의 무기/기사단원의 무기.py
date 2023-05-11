# number는 각 기사 고유 번호
# 기사는 number의 약수 개수만큼 공격력을 가진 무기 구매
# limit는 공격력의 제한수치로 공격력을 초과한다면 power로 대체
def solution(number, limit, power):
    answer = 0

    att = [i+1 for i in range(number)]
    # print(att)
    for i in range(2, number):
        now = att[i]
        div_num = 0
        for j in range(1, int(now**(1/2)) + 1):
            if now % j == 0:
                if j**2 == now:
                    div_num += 1
                else:
                    div_num += 2
        if div_num > limit:
            att[i] = power
        else:
            att[i] = div_num
    # print(att, sum(att))
    answer = sum(att)
    

    # 알고리즘은 맞으나 시간초과
    # att = [i+1 for i in range(number)]
    # for i in range(2, number):
    #     now = att[i]
    #     div_list = []
    #     for j in range(1, now//2+1):
    #         if now % j == 0:
    #             div_list.append(j)
    #             div_list.append(now//j)
    #     div_set = set(div_list)
    #     att[i] = len(div_set)
    # for index, value in enumerate(att):
    #     if value > limit:
    #         att[index] = power
    # answer = sum(att)
    
    
    return answer