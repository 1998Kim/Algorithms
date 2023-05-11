# 벽의 길이가 n : 페인트 칠해짐
# 페인트가 벗겨진 곳이 있음
# 페인트 칠할 곳은 section
# 롤러의 길이 m
def solution(n, m, section):
    answer = 0
    
    # 알고리즘은 맞으나 시간 오래걸림
    # if m == 1:
    #     answer = len(section)
    # else:
    #     check_list = [1 if i not in section else 0 for i in range(n)]
    #     while sum(check_list) != len(check_list):
    #         # option1 : 52점
    #         index = check_list.index(0)
    #         check_list[index: index+m] = [1 for _ in range(m)]
    #         answer += 1
    #         # option2 : 52점
    #         index = section[0]
    #         check_list[index: index+m] = [1 for _ in range(m)]
    #         for i in range(index, index+m):
    #             if i in section:
    #                 section.remove(i)
    #         answer += 1

    #  알고리즘은 맞으나 시간 오래걸림 : 94점
    # if m == 1:
    #     answer = len(section)
    # else:
    #     while section:
    #         now = section[0]
    #         answer += 1
    #         for i in range(now, now+m):
    #             if i in section:
    #                 section.remove(i)
    
    if m == 1:
        answer = len(section)
    else:
        start = section[0]
        for now in section:
            # print(start, now)
            if now >= start:
                start = now + m
                answer += 1


    return answer