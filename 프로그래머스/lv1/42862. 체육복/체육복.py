def solution(n, lost, reserve):
    # n은 전체 수, lost는 잃어버린 학생 번호, reserve는 여벌이 있는 학생 번호
    answer = 0
    
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    # set자료형도 제거됨
    # print(set_reserve)
    # set_reserve.remove(3)
    # print(set_reserve)
    
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i-1)
        elif i + 1 in set_lost:
            set_lost.remove(i+1)

    answer = n - len(set_lost)
    
    return answer