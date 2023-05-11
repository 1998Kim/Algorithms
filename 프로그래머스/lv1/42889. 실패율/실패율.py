# 실패율 = 스테이지 도달 + 클리어X / 도달 플레이어 수

def solution(N, stages): # N: 전체 스테이지 수, stages: 사용자가 현재 멈춘 스테이지 번호
    answer = []
    fail = []
    total_user = len(stages)
    
    for stage in range(1, N+1):
        not_clear_user = 0
        for i in stages:
            if stage == i:
                not_clear_user += 1
        if not_clear_user == 0:
            fail.append(0)
        else:
            fail.append(not_clear_user / total_user)
            total_user -= not_clear_user
    
    sort_fail = sorted(fail, reverse=True)
    
    for i in range(len(sort_fail)):
        answer.append(fail.index(sort_fail[i]) + 1)
        fail[fail.index(sort_fail[i])] = -1

    return answer